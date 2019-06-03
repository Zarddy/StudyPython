
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
