
-- 创建"分组分类"数据表
CREATE TABLE `category` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, -- 分类id
	`parent_id`	INTEGER DEFAULT 0, -- 父级分类id
	`title`	TEXT DEFAULT "", -- 分类名称
	`url`	TEXT DEFAULT "", -- 分类首页路径
	`url_prefix`	TEXT DEFAULT "", -- 分类首页链接前缀
	`thumb`	TEXT DEFAULT "", -- 缩略图路径
	`comment`	TEXT DEFAULT "", -- 备注
	`sort`	INTEGER DEFAULT 9 -- 排序
);


-- 创建"文章"数据表
CREATE TABLE `article` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, -- 文章id
	`category_id`	INTEGER NOT NULL DEFAULT 0, -- 分类id
	`title`	TEXT DEFAULT "", -- 标题
	`thumb`	TEXT DEFAULT "", -- 封面
	`download_links_http`	TEXT DEFAULT "", -- http下载路径（可能多个）
	`download_links_thunder`	TEXT DEFAULT "", -- 迅雷下载路径（可能多个）
	`update_time`	TEXT DEFAULT "", -- 更新时间
	`orig_article_url`	TEXT DEFAULT "", -- 文章原内链地址
	`orig_thumb`	TEXT DEFAULT "" -- 封面原内链地址
);
