#!/usr/bin/python
#coding:utf-8
from flask import Flask ,render_template,request
import json
import requests

app = Flask(__name__)

@app.route('/',methods=['GET','POST','PUT','DELETE'])
def index():
	if request.method == 'GET':
		#name = request.args.get("name") #curl "http://127.0.0.1:888/?name=wd"
		data = request.get_json()
		print data
		return json.dumps(data)
	elif request.method == 'POST':
		#name = request.form.get("name") #curl "http://127.0.0.1:888/" -d 'name=wd' -X POST
		#return "POST User is %s" % name
		data = request.get_json()
		data = json.loads(data)
		name = data['name']
		print data
		print name
		return json.dumps(data)


if __name__=="__main__":
	app.debug=True
	app.run(host='0.0.0.0',port=888)
