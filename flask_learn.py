# -*- coding: utf-8 -*-
from flask import Flask
from flask import make_response
from flask import redirect
from flask import abort

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello world</h1>'


# 第二个参数200 表示返回的状态码：
@app.route('/hello/<name>')
def hello(name):
    return '<h2> hello %s' % name, 200


# 返回response对象，并设置cookie：
@app.route('/return/response')
def return_reponse():
    response = make_response("<h1>This document carries a cookie!</h1>")
    response.set_cookie('answer', '42')
    return response


# 重定向：
@app.route('/redirect')
def return_redirect():
    return redirect('https://www.baidu.com')


# abort 处理错误
@app.route('/abort')
def return_abort():
    abort(403)  # abort(404)


if __name__ == '__main__':
    app.run(debug=True)

# 执行命令:
# export FLASK_APP=flask_learn.py
# flask run
