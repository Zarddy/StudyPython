#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

from miaov.common import HttpHelper
from miaov.parser import CategoryParser
from miaov.parser import OnlineVideoParser

if __name__ == '__main__':

    domain = HttpHelper.get_domain()

    if not domain:
        print('域名获取失败！')

    else:
        print('final domain is ', domain)

        # 获取首页所有分组数据
        CategoryParser.list_all_home_page_category(domain)

        # 获取在线视频所有分组数据
        OnlineVideoParser.list_online_video_category(domain)

        # 获取 "视频下载"分类下的文章列表
        OnlineVideoParser.list_download_video_articles(domain)


# 分组分类：
#
# 在线视频
#     短视频：/shipin/list-短视频.html
#     国产精品：/shipin/list-国产精品.html
#     中文字幕：/shipin/list-中文字幕.html


# 手机下载
#     亚洲电影：/xiazai/list-亚洲电影.html
#     欧美电影：/xiazai/list-欧美电影.html

