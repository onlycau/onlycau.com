#!usr/bin/env python3
# -*- coding: utf-8 -*-
# to do sql语句采用参数方式代替拼接

import pymysql
import json


class Mysql(object):

    def __init__(self):
        self.host = '%'
        self.user = 'web_user'
        self.password = '020202'
        self.db = 'web'
        self.conn = self.__conn()

    def __conn(self):

        conn = pymysql.connect(user=self.user, password=self.password,
                               db=self.db, charset='utf8')
        return conn

    def select_blogs(self, type_list, begin=0, count=5, sort_key='date'):
        # todo 只选择一页的博客 博客条数另外写条查询语句
        more = ''
        for blog_type in type_list:
            more += "or blog_type='%s'" % blog_type
        sql = "select id,title,blog_type,summary,date \
        from blogs where blog_type='%s' %s order by date desc" % (
            type_list[0], more)
        if type_list[0] == 'all':
            sql = "select * from blogs order by date desc "
        # TODO: DictCursor 返回字典结构的代码 待优化
        cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute(sql)
        blogs = cursor.fetchall()
        cursor.close()
        blog_add = [{'count': len(blogs)}]
        if len(blogs) == 0:
            # 未取到数据时 提前返回查询结果
            return json.dumps(blog_add)
        blogs = blogs[begin:begin + count]
        for blog in blogs:
            blog['date'] = str(blog['date'])
        return json.dumps(blog_add + blogs)

    def select_blog_by_id(self, blog_id):
        sql = "select * from blogs where id = %s" % blog_id
        cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute(sql)
        r = cursor.fetchone()
        cursor.close()
        # 判断
        blog = r
        if blog.get('date'):
            blog['date'] = str(blog['date'])
        return json.dumps(blog)

    def new_blog(self, blog):
        cursor = self.conn.cursor()
        sql1 = "insert into blogs(title,blog_type,text,summary) values \
        ('%s','%s','%s', '%s')" % (
            blog['title'], blog['blog_type'],
            pymysql.escape_string(blog['text']), blog['summary'])
        sql2 = "select id from blogs order by id desc limit 1"
        cursor.execute(sql2)
        blog_id = cursor.fetchone()[0] + 1
        sql3 = "create table if not exists comments_%s(\
        `id` int unsigned auto_increment,\
        `username` char(30) not null,\
        `content` char(200) not null,\
        `mailbox` char(50) not null,\
        `date` timestamp null default current_timestamp,\
        primary key(`id`)\
        )engine=innodb default charset=utf8;" % blog_id

        cursor.execute(sql1)
        cursor.execute(sql3)
        self.conn.commit()
        cursor.close()
        return 1

    def edite_blog(self, blog):
        cursor = self.conn.cursor()
        sql1 = "update blogs set title='%s', blog_type='%s',\
        text='%s',summary='%s' where id=%s" % (
            blog['title'], blog['blog_type'],
            blog['text'], blog['summary'], blog['blog_id'])
        if cursor.execute(sql1) == 1:
            self.conn.commit()
            cursor.close()
            return 1
        else:
            cursor.close()
            return 0

    def new_comment(self, table, username, content, mailbox):
        sql = "insert into %s(username, content, mailbox) values \
        ('%s','%s','%s')" % (
            table, username, content, mailbox)
        cursor = self.conn.cursor()
        row_affected = cursor.execute(sql)
        self.conn.commit()
        cursor.close()
        return row_affected

    def select_comments(self, table, begin=0, limit=10):
        cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        sql1 = "select count(*) from %s" % table
        cursor.execute(sql1)
        count = cursor.fetchone().get('count(*)')
        if count == 0:
            return json.dumps([{'count': count}])
        sql2 = "select * from %s order by date desc \
        limit %s,%s" % (table, begin, limit)
        cursor.execute(sql2)
        comments = cursor.fetchall()
        cursor.close()
        for comment in comments:
            comment['date'] = str(comment['date'])
        return json.dumps([{'count': count}] + comments)

    def check_name(self, name):
        sql = "select count(*) from users where name='%s'" % name
        cursor = self.conn.cursor()
        cursor.execute(sql)
        count = cursor.fetchone()
        cursor.close()
        return json.dumps(count)

    def sign_up(self, user):
        sql = "insert into users (name,password,mailbox) values \
        ('%s','%s','%s')" % (
            user['name'], user['password'], user['mailbox'])
        cursor = self.conn.cursor()
        row_affected = cursor.execute(sql)
        if row_affected == 1:
            self.conn.commit()
            cursor.close()
            return row_affected
        else:
            cursor.close()
            return 0

    def sign_in(self, user):
        sql = "select password from users where name='%s'" % user.get('name')
        cursor = self.conn.cursor()
        cursor.execute(sql)
        r = cursor.fetchone()
        cursor.close()
        if r:
            if r[0] == user.get('password'):
                return 1
            else:
                return 0
        else:
            return -1


def test():
    r = Mysql().sign_in({'name':'onlycu','password':'020202'})


if __name__ == '__main__':
    test()
