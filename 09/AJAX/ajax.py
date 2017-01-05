#!/usr/bin/python
#coding:utf-8
from flask import Flask ,render_template,redirect,request,session
import MySQLdb as mysql
from datetime import datetime
import json

datas = mysql.connect(user='root',passwd='123456',db='reboot',charset='utf8')
datas.autocommit(True)
cur = datas.cursor()

app = Flask(__name__)
#import session后初始化加密串
app.secret_key = "qazQAZ!@"


@app.route('/')
def index():
        return render_template('ajax.html')

@app.route('/list')
def list():
        user = {'id':1,'name':'test','age': 18}
        return json.dumps({'code':0,'result':user})
	
@app.route('/add',methods=['GET','POST'])
def add():
        user = dict((k,v[0]) for k ,v in dict(request.form).items())
	print user
        return json.dumps({'code':0,'result':user})

if __name__ == "__main__":
        app.run(host='0.0.0.0',port=888,debug=True)







