
from miaov.common import HttpHelper


def list_online_video_category(domain):
    """
    获取在线视频所有分组数据
    :param domain: 域名
    :return:
    """

    url_home = domain + '/shipin/index.html'
    soup = HttpHelper.get_beautiful_soup(url_home)

    if soup:

        all_cells = soup.find_all("div", class_="cell")
        for cell in all_cells:
            link = cell.a['href'] # 链接地址

            first_index = str(link).index('-')
            last_index = str(link).rindex('.html')

            link_name = link[first_index + 1: last_index] # 链接标题
            thumb = cell.a.img['src'] # 链接缩略图地址

            print('链接：', link)
            print('链接标题：', link_name)
            print('缩略图路径：', thumb)


# TODO 获取 "视频下载"分类下文章分页数
def get_download_video_page_count(domain, title, url_prefix):

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
        page_count = int(last_page_href[last_page_index_first : last_page_index_last])

        return page_count

    else:
        return 0


# TODO 获取 "视频下载"分类下的文章列表
def list_download_video_articles(domain, title, url_prefix):

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


            # # TODO 获取分页控件，通过最后一页的路径获取最大页面数
            # pagination = soup.find('div', class_='pagination')
            # # 最后一页的路径
            # last_page_href = pagination.find_all('a')[-1]['href']
            #
            # last_page_index_first = str(last_page_href).rindex('-') + 1
            # last_page_index_last = str(last_page_href).rindex('.')
            # # 页面总数
            # page_count = int(last_page_href[last_page_index_first : last_page_index_last])
            #
            # print( type(page_count) )

            # print( pagination.find_all('a')[-1]['href'] )
            # print( len(pagination.children) )




            # all_cells = soup.find_all("div", class_="cell")
            # for cell in all_cells:
            #     link = cell.a['href'] # 链接地址
            #
            #     first_index = str(link).index('-')
            #     last_index = str(link).rindex('.html')
            #
            #     link_name = link[first_index + 1: last_index] # 链接标题
            #     thumb = cell.a.img['src'] # 链接缩略图地址
            #
            #     print('链接：', link)
            #     print('链接标题：', link_name)
            #     print('缩略图路径：', thumb)
