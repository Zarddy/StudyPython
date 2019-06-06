from miaov.common import HttpHelper

# "视频下载"资源解析器
from miaov.database import DatabaseManager
from miaov.entity.Article import Article


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
        return int(last_page_href[last_page_index_first: last_page_index_last])

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

        for page in range(1, max_page_count + 1, 1):
            # 得到当前页的全路径
            url_home = domain + url_prefix + title + '-' + str(page) + '.html'
            soup = HttpHelper.get_beautiful_soup(url_home)

            if soup:
                article_list = []

                # 当页记录
                records = soup.select_one('#tpl-img-content').find_all('a')
                for record in records:
                    _title = record['title']  # 文章标题
                    _link = record['href']  # 内链路径
                    _thumb = record.img['data-original']  # 封面（外链）
                    _orig_thumb = record.img['src']  # 封面（内链）
                    _update_time = str(record.span.text).strip()  # 更新日期

                    print(_title, _link, _thumb, _orig_thumb, _update_time)
                    article = get_download_video_article_detail(domain, _title, _link, _thumb, _orig_thumb, _update_time)

                    if article:
                        article_list.append(article.to_sql_insert_data())

                print('# ' * 15)

                if article_list.__len__() > 0:
                    # 按页保存文章记录
                    DatabaseManager.save_many_articles(article_list)


def get_download_video_article_detail(domain, title, link, thumb, orig_thumb, update_time):
    """
    获取文章详情
    :param title: 文章标题
    :param link: 内链路径
    :param thumb: 封面（外链）
    :param orig_thumb: 封面（内链）
    :param update_time: 更新日期
    :return:
    """

    url = domain + link # 文章路径

    soup = HttpHelper.get_beautiful_soup(url)
    if soup:
        all_a = soup.find_all('a', class_='downlink_btn')
        download_links_http = []
        download_links_thunder = []

        for aa in all_a:

            download_link = str(aa['href'])

            if download_link.startswith('thunder://'):
                # 迅雷下载地址
                download_links_thunder.append(download_link)

            else:
                # http下载地址
                download_links_http.append(download_link)

        article = Article(None, 2, title, thumb,
                          download_links_http, download_links_thunder,
                          update_time, link, orig_thumb)

        # 当逐个文章内容保存时，使用以下方法
        # DatabaseManager.save_many_articles(article.to_sql_insert_data())

        return article

    else:
        return None
