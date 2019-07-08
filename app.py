#!usr/bin/env python3
# -*- coding: utf-8 -*-


from flask import Flask, render_template

from orm import Mysql


app = Flask(__name__, static_folder='static/')


# 主页 静态文件路径有Flask static_folder确定
@app.route('/')
def index():
    return app.send_static_file('html/homepage.html')


# 博客页面#静态文件直接相对位置就ok
@app.route('/blog/<name>')
def blog(name):
    text = Mysql().get_blog_by_id(name)[0][0]
    return render_template('blog.html', name=text)


if __name__ == '__main__':
    app.run(debug=True)
