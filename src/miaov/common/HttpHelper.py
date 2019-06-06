
import requests
from bs4 import BeautifulSoup

BASE_DOMAIN = 'https://www.avav32.com'
BASE_HEADERS = { # 请求头部
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Mobile Safari/537.36'
}
BASE_PAYLOAD = {}  # body中的请求参数
BASE_PARAMS = {}  # 添加到url的参数


def get_domain():
    """
    获取经过跳转后的最终域名
    :return: 最终域名
    """

    return get_final_domain(BASE_DOMAIN)


def get_final_domain(url):
    """
    获取经过跳转后的最终域名
    :param url: 初始域名
    :return: 最终域名
    """

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
    """
    获取页面内容
    :param url: 目标路径
    :return: 页面内容
    """

    response = requests.get(url=url, params=BASE_PARAMS, headers=BASE_HEADERS)
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
