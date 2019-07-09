create table if not exists `my_blogs`(
`blog_id` int unsigned auto_increment,
`blog_text` text not null,
`submission_date` date,
primary key(`blog_id`)
)engine=innodb default charset=utf8;
CREATE USER 'web_user'@'%' IDENTIFIED BY '020202';
grant all on web.* to 'web_user'@'%';

create table if not exists `users`(
`user_id` int unsigned auto_increment,
`user_name` char(15) not null,
`user_password` char(15) not null,
primary key(`user_id`)
)engine=innodb default charset=utf8;