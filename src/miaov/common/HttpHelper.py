
import requests
from bs4 import BeautifulSoup

domain = 'https://www.avav32.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Mobile Safari/537.36'
}  # 请求头部
payload = {}  # body中的请求参数
params = {}  # 添加到url的参数
allow_redirects = True  # 是否允许重定向


# 获取经过跳转后的最终域名
def get_domain():
    return get_final_domain(domain)


def get_final_domain(url):
    _response = http_get(url=url)

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


def http_get(url):
    response = requests.get(url=url, params=params, headers=headers)
    response.encoding = 'UTF-8'
    return response


def get_beautiful_soup(url):
    """
    获取 url 路径下的页面，并转换成 BeautifulSoap 对象
    :param url: 指定的页面路径
    :return: BeautifulSoap 对象
    """
    response = http_get(url)

    if response.status_code == 200:

        soup = BeautifulSoup(response.text, 'html.parser')
        return soup

    else:
        return None
