# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template

app = Flask(__name__)


# 未向模板传递参数：
@app.route('/')
def index():
    return render_template('home.html')


# 向模板传递参数：
@app.route('/hello/<name>')
def hello(name):
    comments = ['This is comment 1', 'This is comment 2', 'This is comment 3']
    return render_template('hello.html', username=name, comments=comments)


if __name__ == '__main__':
    app.run(debug=True)

