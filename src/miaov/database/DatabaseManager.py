
import sqlite3

from miaov.entity.Category import Category


def list_categories(parent_id):
    """
    获取分组数据
    :return:
    """

    database = sqlite3.connect('./database/miaov.db')
    cursor = database.cursor()
    cursor.execute("SELECT * FROM category WHERE `parent_id` = '%s'" % str(parent_id))
    rows = cursor.fetchall()
    cursor.close()
    return rows


def list_download_video_categories():
    """
    获取"视频下载-分类分组"列表数据
    :return:
    """

    rows = list_categories(2)
    if len(rows) == 0:
        return []

    categories = []
    for row in rows:
        categories.append(Category(row[0], row[1], row[2], row[3],
                                   row[4], row[5], row[6], row[7]))
    return categories
