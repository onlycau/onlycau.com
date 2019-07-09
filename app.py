#!usr/bin/env python3
# -*- coding: utf-8 -*-


from flask import Flask, render_template, request,session

from orm import Mysql


app = Flask(__name__, static_folder='static/')
app.config['SECRET_KEY'] = 'xxxxxx'


# 主页 静态文件路径有Flask static_folder确定
@app.route('/')
def index():
    return app.send_static_file('html/homepage.html')


# 博客页面#样式文件直接相对位置就ok
@app.route('/blog/<name>')
def blog(name):
    if session.get('logged'):
        text = Mysql().get_blog_by_id(name)[0][0]
        return render_template('blog.html', name=text)
    else:
        return 'sign in first'


@app.route('/sign_in/')
def sign_in():
    return app.send_static_file('html/sign_in.html')


@app.route('/sign_up')
def sign_up():
    return app.send_static_file('html/sign_up.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['name']
        password = request.form['password']
        status_code = Mysql().sign_in(user, password)
        if status_code == -1:
            return 'wrong username'
        if status_code == 0:
            return 'wrong password'
        if status_code == 1:
            session['logged'] = 'xxx'
            return 'nice'
    else:
        return app.send_static_file('html/sign_in.html')


if __name__ == '__main__':
    app.run(debug=True)
