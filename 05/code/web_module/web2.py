#/usr/bin/python 
#coding:utf-8


###第二个web程序,练习form标签,熟悉前端向后端提交数据的流程

from flask import Flask,render_template,redirect,request

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('form.html')

@app.route('/adduser')
def adduser():
	name = request.args.get('name','')
	passw = request.args.get('password','')
	with open('users.txt','a+') as files:
		files.write('%s:%s\n' %(name,passw))
	return redirect("/web4")

@app.route('/web4')
def web4():
       # tmp =  request.args.get('word','web3')
       # age =  request.args.get('age',14)
        #arr = [{'name':'one','age':14},{'name':'two','age':32},{'name':'three','age':9}]
        f = open('users.txt')
        arr = [ line.split(":")  for line in f.read().split('\n') ]
        print arr
       # return render_template('web3_2.html',word = tmp,age = age ,arr = arr)
        return render_template('web3_2.html',arr = arr)

if __name__ == "__main__":
	app.run(host='0.0.0.0',port=888,debug=True)
