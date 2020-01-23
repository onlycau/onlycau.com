--  todo 
--  数据库
-- host = '%'
-- user = 'web_user'
-- password = '020202'
-- db = 'web'
--  用户表
create table if not exists `users`(
`id` int unsigned auto_increment,
`name` char(20) not null,
`password` char(20) not null,
`mailbox` char(30) not null,
`date` timestamp null default current_timestamp,
primary key(`id`)
)engine=innodb default charset=utf8;

--  博客表
create table if not exists `blogs`(
`id` int unsigned auto_increment,
`title` char(100) not null,
`text` text not null,
`summary` varchar(500),
`date` timestamp null default current_timestamp,
`author` char(30) default 'onlycau',
`blog_type` char(30),
`tags` char(100),
`views` int default 0,
primary key(`id`)
)engine=innodb default charset=utf8;

--  评论表
create table if not exists `comments`(
`id` int(8) unsigned auto_increment,
`blog_id` int not null,
`content` char(200) not null,
`from_uid` int(8) not null default 0,
`username` char(30) not null,
`date` timestamp null default current_timestamp,
primary key(`id`)
)engine=innodb default charset=utf8;

--  回复表
create table if not exists `replys`(
`id` int(8) unsigned auto_increment,
`comment_id` int(8) not null,
`content` char(200) not null,
`from_uid` int(8) not null default 0,
`to_uid` int(8) not null default 0,
`to_name` char(30) not null,
`username` char(30) not null,
`date` timestamp null default current_timestamp,
primary key(`id`)
)engine=innodb default charset=utf8;

#xxx数据库访问失败及未获得数据的处理
#CREATE USER 'web_user'@'%' IDENTIFIED BY '020202';
#grant all on web.* to 'web_user'@'%';