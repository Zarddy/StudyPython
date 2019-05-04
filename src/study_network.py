#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import requests


# requests api文档
# https://2.python-requests.org//zh_CN/latest/user/quickstart.html
if __name__ == "__main__":

    target_url = 'https://api.github.com/events'  # 目标内容地址
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Mobile Safari/537.36'
    }  # 请求头部
    payload = {}  # body中的请求参数
    params = {}  # 添加到url的参数
    allow_redirects = True  # 是否允许重定向

    # 网络请求的具体方法
    response = requests.request(method="GET", url=target_url, headers=headers, data=payload, params=params)
    # 简单GET方法
    # response = requests.get(url=target_url, allow_redirects=allow_redirects)

    # 如果响应状态码为200
    if 200 == response.status_code:
        print("响应内容的默认文本编码", response.encoding)

        response.encoding = 'utf-8'  # 修改返回值的文本编码

        print("修改后的文本编码", response.encoding)
        print("响应内容", response.text)
        # print("二进制响应内容", response.content)

        try:
            json_result = response.json()  # JSON响应内容，如果响应内容不是json格式，将会报错
            print("json格式的响应内容", json_result)
        except Exception as e:
            pass

        # 重定向与请求历史
        history = response.history
        print(history)
