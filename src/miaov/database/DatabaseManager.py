
import sqlite3

from miaov.entity.Category import Category


TB_NAME_CATEGORY = 'category'
TB_NAME_ARTICLE = 'article'


def list_categories(parent_id):
    """
    获取分组数据
    :return:
    """

    conn = sqlite3.connect('./database/miaov.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM category WHERE `parent_id` = '%s'" % str(parent_id))
    rows = cursor.fetchall()

    cursor.close()
    conn.close()
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


def save_articles(article_insert_data):
    """
    保存文章，保存单个文章数据
    :param article_insert_data: 文章内容
    :return:
    """

    conn = sqlite3.connect('./database/miaov.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO `%s` (`category_id`, `title`, `thumb`, `download_links_http`, `download_links_thunder`,"
                   "`update_time`, `orig_article_url`, `orig_thumb`) VALUES (?, ?, ?, ?, ?, ?, ?, ?)" % TB_NAME_ARTICLE, article_insert_data)

    conn.commit()
    cursor.close()
    conn.close()


def save_many_articles(article_insert_data_list):
    """
    保存文章，一次保存多个数据记录
    :param article_insert_data_list: 文章内容数据列表
    :return:
    """

    conn = sqlite3.connect('./database/miaov.db')
    cursor = conn.cursor()

    cursor.executemany("INSERT INTO `%s` (`category_id`, `title`, `thumb`, `download_links_http`, `download_links_thunder`,"
                       " `update_time`, `orig_article_url`, `orig_thumb`) VALUES (?, ?, ?, ?, ?, ?, ?, ?)" % TB_NAME_ARTICLE, article_insert_data_list)

    conn.commit()
    cursor.close()
    conn.close()
