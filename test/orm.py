#!usr/bin/env python3
# -*- coding: utf-8 -*-


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

    def select_blogs(self, blogs_type, begin=0, count=5, sort_key='date'):
        # todo 只选择一页的博客 博客条数另外写条查询语句
        sql = "select * from blogs where blog_type='%s' order by date desc" % (
            blogs_type)
        if blogs_type == 'all':
            sql = "select * from blogs order by date desc "
        # TODO: DictCursor 返回字典结构的代码 待优化
        cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute(sql)
        blogs = cursor.fetchall()
        blog_add = [{'blog_count': len(blogs)}]
        blogs = blogs[begin:begin + count]
        for blog in blogs:
            blog['date'] = str(blog['date'])
            blog['text'] = blog['text'][0:100]
        return json.dumps(blog_add + blogs)

    def select_blog_by_id(self, blog_id):
        sql = "select * from blogs where id = %s" % blog_id
        cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute(sql)
        r = cursor.fetchone()
        # 判断
        blog = r
        if blog.get('date'):
            blog['date'] = str(blog['date'])
        return json.dumps(blog)

    def new_blog(self, blog):
        sql = "insert into blogs(title,blog_type,text,date) values \
        ('%s','%s','%s','%s')" % (
            blog['title'], blog['blog_type'],
            blog['text'], '2019-07-31 19:13:00')
        cursor = self.conn.cursor()
        cursor.execute(sql)
        self.conn.commit()
        cursor.close()
        return 1

    def new_web_comment(self, username, content, mailbox):
        sql = "insert into web_comments(username, content, mailbox) values \
        ('%s','%s','%s')" % (
            username, content, mailbox)
        cursor = self.conn.cursor()
        row_affected = cursor.execute(sql)
        self.conn.commit()
        cursor.close()
        return row_affected

    def select_web_comments(self, begin=0, limit=10):
        cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        sql = "select count(*) from web_comments"
        cursor.execute(sql)
        count = cursor.fetchone()
        sql = "select * from web_comments order by date desc \
        limit %s,%s" % (begin, limit)
        cursor.execute(sql)
        web_comments = cursor.fetchall()
        for comment in web_comments:
            comment['date'] = str(comment['date'])
        return json.dumps([{'count': count}] + web_comments)


def test():
    r = Mysql().select_web_comments()
    print(r)


if __name__ == '__main__':
    test()
