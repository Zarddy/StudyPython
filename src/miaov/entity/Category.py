# 分组数据
class Category:

    def __init__(self):
        super().__init__()

    def __init__(self, id, parent_id, title, url, thumb, comment):
        self.__init__(id, parent_id, title, url, thumb, comment, sort=9)

    def __init__(self, id, parent_id, title, url, thumb, comment, sort):
        self.id = id
        self.parent_id = parent_id
        self.title = title
        self.url = url
        self.thumb = thumb
        self.comment = comment
        self.sort = sort

