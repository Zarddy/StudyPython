
class Category:
    """
    分组数据
    """

    def __init__(self):
        self.__init__('', '', '', '', '', '', '')

    def __init__(self, id, parent_id, title, url, url_prefix, thumb, comment):
        self.__init__(id, parent_id, title, url, url_prefix, thumb, comment, sort=9)

    def __init__(self, id, parent_id, title, url, url_prefix, thumb, comment, sort):
        self.id = id
        self.parent_id = parent_id
        self.title = title
        self.url = url
        self.url_prefix = url_prefix
        self.thumb = thumb
        self.comment = comment
        self.sort = sort
