create table if not exists `blogs`(
`id` int unsigned auto_increment,
`title` char(100) not null,
`text` text not null,
`summary` varchar(1000),
`date` timestamp null default current_timestamp,
`author` char(30) default 'onlycau',
`family` char(30),
`tags` char(100),
`views` int default 0,
primary key(`id`)
)engine=innodb default charset=utf8;
create table if not exists `users`(
`user_id` int unsigned auto_increment,
`user_name` char(15) not null,
`user_password` char(15) not null,
primary key(`user_id`)
)engine=innodb default charset=utf8;
#CREATE USER 'web_user'@'%' IDENTIFIED BY '020202';
#grant all on web.* to 'web_user'@'%';
