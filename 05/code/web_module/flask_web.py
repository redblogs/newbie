#/usr/bin/python
#coding:utf-8

from flask import Flask ,request,render_template,redirect

from getUser import readUser

##new app

app = Flask(__name__)

@app.route('/')
def  index():
	return  "hello index"

@app.route('/test')
def  test():
	return  "hello test"

##获取参数import request 
##request里面包含一次网络请求所有的内容
##request.args是一个类似dict的数据结构。
@app.route('/webone')
def webone():
	print request.args
	print 'requst.arge type is %s' %(type(request.args))
	return "Welcome to webone"
'''
##webone运行结果
ImmutableMultiDict([('name', u'aa')])
requst.arge type is <class 'werkzeug.datastructures.ImmutableMultiDict'>
192.168.137.1 - - [29/Nov/2016 16:03:24] "GET /webone?name=aa HTTP/1.1" 200 -
'''

@app.route('/webtwo')
def webotwo():
	tmp =  request.args.get('word','webtwo')
	return "The search word is %s" %tmp

##using render_template
@app.route('/web3')
def web3():
	tmp =  request.args.get('word','web3')
	age =  request.args.get('age',14)
	#arr = [{'name':'one','age':14},{'name':'two','age':32},{'name':'three','age':9}]
	arr = readUser('users.txt')
	print arr
	return render_template('web3_1.html',word = tmp,age = age ,arr = arr)

'''
##注意web4中f.read()的结果为字符串
In [21]: f = open('users.txt')

In [22]: f.read()
Out[22]: 'AA:123\nBB:32\ncc:1231\nkk:33\nAA1:11\ntt:12\nwoniu:11\n'
'''
@app.route('/web4')
def web4():
	tmp =  request.args.get('word','web3')
	age =  request.args.get('age',14)
	#arr = [{'name':'one','age':14},{'name':'two','age':32},{'name':'three','age':9}]
	f = open('users.txt')
	arr = [ line.split(":")  for line in f.read().split('\n') ]
	print arr
	return render_template('web3_2.html',word = tmp,age = age ,arr = arr)


##实现跳转功能,import redirect 函数
@app.route('/web5')
def web5():
	role = request.args.get('role','')
	if role == 'admin':
		return redirect('/test')
	else :
		return "please login"
if __name__ == "__main__":
	app.run(host='0.0.0.0',port=888,debug=True)
