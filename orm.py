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


def test():
    a='''      <h1>07/01-07/07第一周学习大概</h1>
      <div class="blog">
        head first and csscss回顾了一下基础，熟悉了样式的基本使用，熟练度有待项目中提高。<br>
        目前需重点巩固方向：
        <li>盒模型 content area-padding-border-margin</li>
        <li>选择器 </li>
        <li>布局与定位</li><br>
        js高级程序设计跳着看了半本，下周粗略过完第一遍，个人博客1.0搭建完后再细看理解一遍。<br>
        <li>对象的几个构造模式 数组、对象的生存周期等</li><br>
        随时都需要注意熟悉的一些细节：<br>
        <li>语义化 对象 标签命名 代码布局 注释（大小写）</li>
        <li>重用</li><br>
        <h2>下周计划</h2>
        <p>
          js高级程序设计过完第一遍<br>
          个人博客beta搭完:<br>
          主页 评论 登录 注册 后台 
        </p>

      <div>'''
    print(Mysql().save_blog(a))


if __name__ == '__main__':
    test()
