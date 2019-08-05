#!usr/bin/env python3
# -*- coding: utf-8 -*-


from flask import Flask, render_template, request, session
from flask_cors import CORS

from orm import Mysql


app = Flask(__name__)
app.config['SECRET_KEY'] = 'xxxxxx'


# 请求文章摘要的后台方法，默认为最新5篇文章
@app.route('/api/blog/select_blogs', methods=['GET'])
def select_blogs():
    blog_type = 'all'
    begin = 0

    if request.args.get('blog_type'):
        bh = request.args.get('blog_type')
        if len(bh) > 11:
            blog_type = bh.split(',')
        else:
            blog_type = []
            blog_type.append(bh)
    if request.args.get('begin'):
        begin = int(request.args.get('begin'))
    blogs = Mysql().select_blogs(blog_type, begin)
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


@app.route('/api/new_comment')
def new_web_comment():
    username = request.args.get('username')
    text = request.args.get('content')
    mailbox = request.args.get('mailbox')
    table = request.args.get('table')
    rows_efected = Mysql().new_comment(table, username, text, mailbox)
    return str(rows_efected)


@app.route('/api/comments')
def select_comments():
    begin = request.args.get('begin')
    table = request.args.get('table')
    web_comments = Mysql().select_comments(table, begin)
    return web_comments

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
