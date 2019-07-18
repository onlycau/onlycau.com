#!usr/bin/env python3
# -*- coding: utf-8 -*-


from flask import Flask, render_template, request, session
from flask import jsonify

from orm import Mysql


app = Flask(__name__, static_folder='static/')
app.config['SECRET_KEY'] = 'xxxxxx'


# 主页 静态文件路径有Flask static_folder确定
@app.route('/')
def index():
    return render_template('homepage.html')


@app.route('/get_blogs/', methods=['GET'])
def get_blogs():
    sort = 'homepage'
    if request.args.get('sort'):
        sort = request.args.get('sort')
    blogs = Mysql().get_blog_by_sort(sort)
    return blogs


if __name__ == '__main__':
    app.run(debug=True)
