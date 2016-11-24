#!/usr/bin/python
#coding:utf-8
from flask import Flask ,render_template,request
import json

app = Flask(__name__)

@app.route('/',methods=['GET','POST','PUT','DELETE'])
def index():
	if request.method == 'GET':
		name = request.args.get("name") #curl "http://127.0.0.1:888/?name=wd"
		return "GET User is %s" % name
	elif request.method == 'POST':
		name = request.form.get("name") #curl "http://127.0.0.1:888/" -d 'name=wd' -X POST
		return "POST User is %s" % name
	elif request.method == 'PUT':
		name = request.form.get("name") #curl "http://127.0.0.1:888/" -d 'name=wd' -X PUT
		return "PUT User is %s" % name
	elif request.method == 'DELETE':
		name = request.form.get("name") #curl "http://127.0.0.1:888/" -d 'name=wd' -X DELETE
		return "DELETE User is %s" % name

@app.route('/<string:username>',methods=['GET','PUT','POST'])
def test(username):
	if request.method == 'GET':##curl "http://127.0.0.1:888/wd?age=18"
		age = request.args.get('age')
	elif request.method == 'POST':##curl "http://127.0.0.1:888/wd" -d 'age=18' -X POST
		age = request.form.get('age')
	elif request.method == 'PUT':##curl "http://127.0.0.1:888/wd" -d 'age=18' -X PUT
		age = request.form.get('age')
	return "User is %s ,and age is %s" % (username,age)

if __name__=="__main__":
	app.debug=True
	app.run(host='0.0.0.0',port=888)
