
from miaov.common import HttpHelper

"""
分类解析器
"""


def list_all_home_page_category(domain):
    """
    获取首页所有分组数据
    :param domain: 域名
    :return:
    """

    url_home = domain + '/index/home.html'

    soup = HttpHelper.get_beautiful_soup(url_home)
    if soup:
        all_row_item = soup.find_all("div", class_="row-item")

        for row_item in all_row_item:
            row_item_title = row_item.find('div', class_='row-item-title')

            print('父级分类：', row_item_title.text)

            row_item_content = row_item.find('ul', class_='row-item-content')

            for row in row_item_content.find_all('a'):
                print('-' * 15)
                print('子级链接：', row['href'])
                print('子级名称：', str(row.text).strip())

            print('#' * 15)
