create database web;
use web;
create table if not exists `my_blogs`(
`blog_id` int unsigned auto_increment,
`blog_text` text not null,
`submission_date` date,
primary key(`blog_id`)
)engine=innodb default charset=utf8;
CREATE USER 'web_user'@'%' IDENTIFIED BY '020202';
grant all on web.* to 'web_user'@'%';
