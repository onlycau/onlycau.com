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

        conn = pymysql.connect(user=self.user, password=self.password, db=self.db, charset='utf8')
        return conn

    def select_blogs(self, family, begin=0, count=2, sort_key='date'):
        sql = "select * from blogs where type='%s' order by date desc" % (family)
        if family == 'all':
            sql = "select * from blogs order by date desc "
        # DictCursor 返回字典结构的代码 待修改
        cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute(sql)
        blogs = cursor.fetchall()[begin:begin + count]
        for blog in blogs:
            blog['date'] = str(blog['date'])
        return json.dumps(blogs)

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


def test():
    blogs = Mysql().select_blogs('all', 5, 2)
    print(blogs)
    blog = Mysql().select_blog_by_id(3)
    print(blog)


if __name__ == '__main__':
    test()
