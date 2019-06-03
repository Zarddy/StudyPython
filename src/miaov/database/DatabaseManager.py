
import sqlite3


def list_categories(self):
    """
    获取分组数据
    :param self:
    :return:
    """

    database = sqlite3.connect('./database/miaov.db')
    self.cursor = database.cursor()
    self.cursor.execute('SELECT * FROM category')
    return self.cursor.fetchall()
