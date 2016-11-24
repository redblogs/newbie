#!/usr/bin/env python
#coding:utf-8
from flask import Flask,render_template,request
from flask_jsonrpc import JSONRPC
import json

app = Flask(__name__)
jsonrpc = JSONRPC(app, '/api')

@jsonrpc.method('App.index')         #ÏӦÎ²ÎýÄethod
def index():                                 
    return "hello baby!"

@jsonrpc.method('App.name')         #ÏӦÓָ¶¨²ÎýÄethod
def name(name):
    return 'hello %s' %  name 

@jsonrpc.method('App.user')        #ÏӦÓ²»¶¨²ÎýÄethod£¬×³£Ó
def user(**kwargs):
    data = {}
    data['name'] = kwargs.get('name',None)
    data['age'] = kwargs.get('age',None)
    return 'I am  %s,age is %s' % (data['name'],data['age'])

@jsonrpc.method('App.users')           
def users(**kwargs):
    data = request.get_json()   #È¹ûÈµĲÎý࣬ kwargs.get()µķ½ʽ¿ÉܱȽϷѾ¢£¬¿ÉÔet_json()»ñùÊ£¬ͨ¹ýбí·½ʽ¼õú
    data['name'] = data['params']['name']
    data['age'] = data['params']['age']
    return 'I am  %s,age is %s' % (data['name'],data['age'])


if __name__=='__main__':
    app.debug=True
    app.run(host='0.0.0.0',port=888)
