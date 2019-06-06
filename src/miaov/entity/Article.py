
class Article:
    """
    文章数据
    """

    def __init__(self):
        self.__init__(None, 0, '', '', '', '', '', '', '')

    def __init__(self, id, category_id, title, thumb,
                 download_links_http, download_links_thunder,
                 update_time, orig_article_url, orig_thumb):
        self.id = id
        self.category_id = category_id
        self.title = title
        self.thumb = thumb
        self.download_links_http = download_links_http
        self.download_links_thunder = download_links_thunder
        self.update_time = update_time
        self.orig_article_url = orig_article_url
        self.orig_thumb = orig_thumb

    def to_sql_insert_data(self):
        return (self.category_id, self.title, self.thumb,
                 str(self.download_links_http), str(self.download_links_thunder),
                 self.update_time, self.orig_article_url, self.orig_thumb)
