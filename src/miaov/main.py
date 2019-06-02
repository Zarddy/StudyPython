#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

import requests

domain = ''
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Mobile Safari/537.36'
}  # 请求头部
payload = {}  # body中的请求参数
params = {}  # 添加到url的参数
allow_redirects = True  # 是否允许重定向


def get_final_domain(url):
    _response = requests.get(url=url, params=params, headers=headers)

    if _response.status_code == 200:
        _new_url = str(_response.url)

        print('new_url:', _new_url)

        if _new_url.__eq__(url):
            return url

        else:
            return get_final_domain(_new_url)

    else:
        return 'nothing'


if __name__ == '__main__':

    domain = get_final_domain(domain)
    print('final domain is ', domain)
