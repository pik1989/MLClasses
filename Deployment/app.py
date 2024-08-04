# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)

# URL Binding
@app.route('/')
def hello():
    return("I am SPARTA!!")

@app.route('/page2')
def hello_2():
    return("I am ADMIN!!")

@app.route('/admin')
def hello_4():
    return("This is a restricted page!!")

app.run(port=8000)

