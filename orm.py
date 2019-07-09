#!usr/bin/env python3
# -*- coding: utf-8 -*-


import pymysql


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

    def get_blog_by_id(self, id):
        sql = 'select blog_text from my_blogs where blog_id=%s' % id
        cursor = self.conn.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

    def save_blog(self, text):
        sql = 'insert into my_blogs (blog_text) values (\'%s\')' % text
        cursor = self.conn.cursor()
        rows = 0
        rows = cursor.execute(sql)
        self.conn.commit()
        cursor.close()
        return rows

    def sign_up(self, name, password):
        cursor = self.conn.cursor()
        sql1 = "select user_id from users where user_name='%s'" % name
        sql2 = "insert into users (user_name,user_password) values ('%s','%s')" % (name, password)
        print(sql2)
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

    a = Mysql().sign_up('c5123345', '2ld22255')
    print(a)


if __name__ == '__main__':
    test()
