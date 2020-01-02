#!usr/bin/env python3
# -*- coding: utf-8 -*-


from flask import Flask, request, session
from flask_cors import CORS

import json

from orm import Mysql

app = Flask(__name__, static_url_path='')
app.config['SECRET_KEY'] = 'xxxxxx'




# 请求文章摘要的后台方法，默认为最新5篇文章
@app.route('/api/blog/select_blogs', methods=['GET'])
def select_blogs():
    blog_type = 'all'
    begin = 0

    if request.args.get('blog_type'):
        bh = request.args.get('blog_type')
        blog_type = bh.split(',')
    if request.args.get('begin'):
        begin = int(request.args.get('begin'))
    blogs = Mysql().select_blogs(blog_type, begin)
    return blogs


@app.route('/api/blog/select_blog', methods=['GET'])
def select_blog():
    blog_id = request.args.get('blog_id')
    blog = Mysql().select_blog_by_id(blog_id)
    return blog


@app.route('/api/blog/new', methods=['POST'])
def new_blog():
    blog = request.get_json()
    if blog:
        Mysql().new_blog(blog)
    return "nice"


@app.route('/api/blog/edite', methods=['POST'])
def edite_blog():
    blog = request.get_json()
    if blog.get('password') == '1961':
        r = Mysql().edite_blog(blog)
        if r == 1:
            return '1'
        else:
            return '-1'
    else:
        return '0'


@app.route('/api/new_comment',methods=['POST'])
def new_web_comment():
    comment = request.get_json()
    print(comment)
    rows_efected = Mysql().new_comment(comment['table_name'], comment['username'], comment['content'], comment['mailbox'])
    return str(rows_efected)


@app.route('/api/comments')
def select_comments():
    begin = request.args.get('begin')
    table_name = request.args.get('table_name')
    web_comments = Mysql().select_comments(table_name, begin)
    return web_comments


# 注册
# 注意 fals直接返回字符串时 实际客户端接收到的是字符串内包裹的内容
@app.route('/user/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'GET':
        if request.args.get('name'):
            name = request.args.get('name')
            count = Mysql().check_name(name)
            return count
    if request.method == 'POST':
        user = request.get_json()
        r = Mysql().sign_up(user)
        if r == 1:
            return '1'
        else:
            return '0'


# # 登录 跨域时cookie处理有变化 暂时无效
@app.route('/user/sign_in', methods=['POST'])
def sign_in():
    session['logged'] = True
    user = request.get_json()
    if user:
        r = Mysql().sign_in(user)
        if r == 1:
            session['logged'] = user['name']
            return '1'
        else:
            return '0'
    else:
        return '-1'


@app.route('/user/is_logged')
def is_logged():
    if 'logged' in session:
        return json.dumps({'name': session['logged'], 'logged': 1})
    else:
        return json.dumps({'name': 'onlycau', 'logged': 0})


@app.route('/user/sign_out/')
def sign_out():
    if session.get('logged'):
        session.pop('logged')
        session.clear
        return '1'
    else:
        return '1'


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/home')
def home():
    return app.send_static_file('home.html')


if __name__ == '__main__':
    # CORS处理跨域
    CORS(app, supports_credentials=True)
    app.run(debug=True)
