#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

import requests
from bs4 import BeautifulSoup


domain = 'https://www.xxx.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Mobile Safari/537.36'
}  # 请求头部
payload = {}  # body中的请求参数
params = {}  # 添加到url的参数
allow_redirects = True  # 是否允许重定向


# 获取经过跳转后的最终域名
def get_final_domain(url):
    _response = requests.get(url=url, params=params, headers=headers)

    if _response.status_code == 200:
        _new_url = str(_response.url)

        if '/'.__eq__(_new_url[-1]):
            _new_url = _new_url[:-1]

        if _new_url.__eq__(url):
            return url

        else:
            return get_final_domain(_new_url)
    else:
        return None


# 获取所有分组数据
def list_all_category(html_doc):
    soup = BeautifulSoup(html_doc, 'html.parser')
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



if __name__ == '__main__':

    domain = get_final_domain(domain)

    if not domain:
        print('域名获取失败！')

    else:
        print('final domain is ', domain)

        domain += '/index/home.html'

        response = requests.get(url=domain, params=params, headers=headers)
        response.encoding = 'UTF-8'

        if response.status_code == 200:
            # print( response.text )

            # 获取所有分组数据
            list_all_category(response.text)
