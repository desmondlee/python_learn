# -*- coding: utf-8 -*-
from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello world</h1>'


@app.route('/hello/<name>')
def hello(name):
    return '<h2> hello %s' % name


if __name__ == '__main__':
    app.run(debug=True)


# 执行命令:
# export FLASK_APP=flask_learn.py
# flask run