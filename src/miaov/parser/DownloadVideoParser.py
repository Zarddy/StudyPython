
from miaov.common import HttpHelper

# "视频下载"资源解析器
from miaov.database import DatabaseManager


def get_download_video_page_count(domain, title, url_prefix):
    """
    获取 "视频下载"分类下文章分页数
    :param domain: 域名
    :param title: 分类名称
    :param url_prefix: 分类列表页路径前缀
    :return: 该分类的最大分页数
    """

    url_home = domain + url_prefix + title + '.html'
    soup = HttpHelper.get_beautiful_soup(url_home)

    if soup:

        # 获取分页控件，通过最后一页的路径获取最大页面数
        pagination = soup.find('div', class_='pagination')
        # 最后一页的路径
        last_page_href = pagination.find_all('a')[-1]['href']

        last_page_index_first = str(last_page_href).rindex('-') + 1
        last_page_index_last = str(last_page_href).rindex('.')
        # 页面总数
        return int(last_page_href[last_page_index_first : last_page_index_last])

    else:
        return 0


def list_download_video_articles(domain, title='', url_prefix=''):
    """
    获取 "视频下载"分类下的文章列表
    :param domain: 域名
    :param title: 分类名称
    :param url_prefix: 分类列表页路径前缀
    :return: 文章列表数据
    """

    if title.strip().__len__() == 0 and url_prefix.strip().__len__() == 0:
        categories = DatabaseManager.list_download_video_categories()

        if len(categories) > 0:
            for category in categories:
                list_download_video_articles(domain, category.title, category.url_prefix)

    else:
        # 获取最大分页数
        max_page_count = get_download_video_page_count(domain, title, url_prefix)

        for i in range(1, max_page_count + 1, 1):
            url_home = domain + url_prefix + title + '-' + str(i) + '.html'
            soup = HttpHelper.get_beautiful_soup(url_home)

            if soup:
                # 当页记录
                records = soup.select_one('#tpl-img-content').find_all('a')
                for record in records:
                    _title = record['title']
                    _link = record['href']
                    _thumb = record.img['data-original']
                    _thumb_src = record.img['src']
                    _update_date = str(record.span.text).strip()

                    print(_title, _link, _thumb, _thumb_src, _update_date)
                print('# ' * 15)
