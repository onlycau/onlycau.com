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
        return render_template('homepage.html', name=session['logged'])
    else:
        return render_template('homepage.html', name='登录')


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
            return render_template('homepage.html', name=session['logged'])
    else:
        return app.send_static_file('html/sign_in.html')


@app.route('/has_sign_in/')
def has_sign_in():
    if session.get('logged'):
        return session['logged']
    else:
        return '-1'


if __name__ == '__main__':
    app.run(debug=True)
