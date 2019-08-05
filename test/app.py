#!usr/bin/env python3
# -*- coding: utf-8 -*-


from flask import Flask, request
from flask_cors import CORS

from orm import Mysql


app = Flask(__name__)
app.config['SECRET_KEY'] = 'xxxxxx'


# 请求文章摘要的后台方法，默认为最新2篇文章
@app.route('/api/blog/select_blogs', methods=['GET'])
def select_blogs():
    blogs_type = 'all'
    begin = 0
    if request.args.get('blogs_type'):
        blogs_type = request.args.get('blogs_type')
    if request.args.get('begin'):
        begin = int(request.args.get('begin'))
    blogs = Mysql().select_blogs(blogs_type, begin)
    return blogs


@app.route('/api/blog/select_blog', methods=['GET'])
def select_blog():
    blog_id = request.args.get('blog_id')
    blog = Mysql().select_blog_by_id(blog_id)
    print(blog)
    return blog


@app.route('/api/blog/new', methods=['POST'])
def new_blog():
    blog = request.get_json()
    if blog:
        Mysql().new_blog(blog)
    return blog


@app.route('/api/new_web_comment')
def new_web_comment():
    username = request.args.get('username')
    text = request.args.get('content')
    mailbox = request.args.get('mailbox')
    rows_efected = Mysql().new_web_comment(username, text, mailbox)
    return str(rows_efected)


@app.route('/api/select_web_comments')
def select_web_comments():
    begin = request.args.get('begin')
    web_comments = Mysql().select_web_comments(begin)
    return web_comments


@app.route('/')
def index():
    return app.send_static_file('index.html')
# # 登录
# @app.route('/sign_in/', methods=['GET', 'POST'])
# def sign_in():
#     if request.method == 'POST':
#         user = request.form['name']
#         password = request.form['password']
#         status_code = Mysql().sign_in(user, password)
#         if status_code == -1:
#             return 'wrong username'
#         if status_code == 0:
#             return 'wrong password'
#         if status_code == 1:
#             session['logged'] = user
#             return app.send_static_file('html/homepage.html')
#     else:
#         return app.send_static_file('html/sign_in.html')


# # 注册
# @app.route('/sign_up/', methods=['GET', 'POST'])
# def sign_up():
#     if request.args.get('name'):
#         name = request.args.get('name')
#         password = request.args.get('password')
#         status_code = Mysql().sign_up(name, password)
#         if status_code == 1:
#             return '1'
#         else:
#             return '-1'
#     else:
#         return app.send_static_file('html/sign_up.html')


# # 退出
# @app.route('/sign_out/')
# def sign_out():
#     if session.get('logged'):
#         session.pop('logged')
#         session.clear
#         return app.send_static_file('html/homepage.html')
#     else:
#         return '退出失败'


# # 是否登录判断 客户端每次访问时会额外请求一次 获取登录状态
# @app.route('/has_sign_in/')
# def has_sign_in():
#     if session.get('logged'):
#         return session['logged']
#     else:
#         return '-1'


if __name__ == '__main__':
    # CORS处理跨域
    CORS(app, supports_credentials=True)
    app.run(debug=True)
