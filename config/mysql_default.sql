--  todo 
--  数据库

--  表
--  博客表
--  评论表
create table if not exists `web_comments`(
`id` int unsigned auto_increment,
`username` char(30) not null,
`content` char(200) not null,
`hide` int default 0,
`date` timestamp null default current_timestamp,
primary key(`id`)
)engine=innodb default charset=utf8;
#xxx数据库访问失败及未获得数据的处理
