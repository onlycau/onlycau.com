#!usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask
from flask import request


app = Flask(__name__, static_url_path='')


@app.route('/', methods=['GET', 'POST'])
def home():
    return app.send_static_file('templates/note.html')


if __name__ == '__main__':
    app.run()
