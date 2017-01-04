#!/usr/bin/python
#coding:utf-8

from flask import Flask,request,render_template,redirect

app = Flask(__name__)

@app.route('/')
def index():
	return redirect('/login')

@app.route('/login',methods=["GET",'POST'])
def login():
	if request.method == "POST":
		print request.method
		print request.form.get("name",None)
		print request.form
		tmp_post = dict(request.form)
		print tmp_post
		print dict( (k,v[0]) for k ,v in tmp_post.items())

	#else:
	#	print request.method
	#	print request.args.get("username",None)
	#	print request.args
	#	tmp_get = dict(request.args)
	#	print dict( (k,v[0]) for k ,v in tmp_get.items())
	return render_template('login.html')

if __name__ == "__main__":
	app.run(host='0.0.0.0',port=888,debug = True)
