--  todo 
--  数据库

--  表
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
create table if not exists `web_comments`(
`id` int unsigned auto_increment,
`username` char(30) not null,
`content` char(200) not null,
`mailbox` char(30) not null,
`date` timestamp null default current_timestamp,
primary key(`id`)
)engine=innodb default charset=utf8;
#xxx数据库访问失败及未获得数据的处理
