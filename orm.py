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

    def get_blog_by_sort(self, sort, count=5):
        sql = "select * from blogs where sort='%s' order by date desc  limit %d" % (sort, count)
        if sort == 'homepage':
            sql = "select * from blogs order by date desc limit %d" % (count)
        cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute(sql)
        r = cursor.fetchall()
        for i in r:
            if i.get('date'):
                i['date'] = str(i['date'])
        return json.dumps(r)

    def sign_up(self, name, password):
        cursor = self.conn.cursor()
        sql1 = "select user_id from users where user_name='%s'" % name
        sql2 = "insert into users (user_name,user_password) values ('%s','%s')" % (name, password)
        if cursor.execute(sql1) != 0:
            cursor.close()
            return -1
        else:
            rows = cursor.execute(sql2)
            self.conn.commit()
            cursor.close()
            return rows

    def sign_in(self, name, password):
        cursor = self.conn.cursor()
        sql = "select user_password from users where user_name='%s'" % name
        if cursor.execute(sql) == 0:
            return -1
        if cursor.fetchone()[0] == password:
            return 1
        else:
            return 0


def test():
    pass


if __name__ == '__main__':
    test()
