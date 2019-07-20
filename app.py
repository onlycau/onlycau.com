#!usr/bin/env python3
# -*- coding: utf-8 -*-


from flask import Flask, render_template, request, session

from orm import Mysql


app = Flask(__name__)
app.config['SECRET_KEY'] = 'xxxxxx'


# 主页
@app.route('/')
def index():
    if session.get('logged'):
        return app.send_static_file('html/homepage.html')
    else:
        return app.send_static_file('html/homepage.html')


# 请求文章摘要的后台方法，默认为最新5篇文章
@app.route('/get_blogs/', methods=['GET'])
def get_blogs():
    sort = 'homepage'
    if request.args.get('sort'):
        sort = request.args.get('sort')
    blogs = Mysql().get_blog_by_sort(sort)
    return blogs


# 登录
@app.route('/sign_in/', methods=['GET', 'POST'])
def sign_in():
    if request.method == 'POST':
        user = request.form['name']
        password = request.form['password']
        status_code = Mysql().sign_in(user, password)
        if status_code == -1:
            return 'wrong username'
        if status_code == 0:
            return 'wrong password'
        if status_code == 1:
            session['logged'] = user
            return app.send_static_file('html/homepage.html')
    else:
        return app.send_static_file('html/sign_in.html')


# 注册
@app.route('/sign_up/', methods=['GET', 'POST'])
def sign_up():
    if request.args.get('name'):
        name = request.args.get('name')
        password = request.args.get('password')
        status_code = Mysql().sign_up(name, password)
        if status_code == 1:
            return '1'
        else:
            return '-1'
    else:
        return app.send_static_file('html/sign_up.html')


# 退出
@app.route('/sign_out/')
def sign_out():
    if session.get('logged'):
        session.pop('logged')
        session.clear
        print(session.get('logged'))
        return '1'
    else:
        return '-1'


# 是否登录判断 客户端每次访问时会额外请求一次 获取登录状态
@app.route('/has_sign_in/')
def has_sign_in():
    if session.get('logged'):
        return session['logged']
    else:
        return '-1'


if __name__ == '__main__':
    app.run(debug=True)
