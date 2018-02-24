# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap  #需要执行 pip3 install flask-bootstrap 安装扩展

app = Flask(__name__)
bootstrap = Bootstrap(app)


# 未向模板传递参数：
@app.route('/')
def index():
    return render_template('home.html')


# 向模板传递参数：
@app.route('/hello/<name>')
def hello(name):
    comments = ['This is comment 1', 'This is comment 2', 'This is comment 3']
    return render_template('hello.html', username=name, comments=comments)


# block 模板继承
@app.route('/block')
def return_block():
    return render_template('my_block.html')


# bootstrap 使用：
@app.route('/bootstrap/<username>')
def return_bootstrap(username):
    return render_template('my_bootstrap.html', name=username)


if __name__ == '__main__':
    app.run(debug=True)

