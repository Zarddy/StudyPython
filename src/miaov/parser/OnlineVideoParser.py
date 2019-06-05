
from miaov.common import HttpHelper

# "在线视频"资源解析器


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
