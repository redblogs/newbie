#/usr/bin/python 
#coding:utf8

from flask import Flask
from flask import request,render_template,redirect
import time
from datas import *

app = Flask(__name__)

@app.route('/adduser', methods=['GET','POST'])
def adduser():
	if request.method == 'POST':
		fields = ['status', 'role', 'name', 'mobile', 'password', 'name_cn', 'email']
		#name = request.form.get('name','') #获取单一前端传递的数据
		user = request.form		    #获取所有的前端传递的数据,类似字典
		tmp = {}
		for i in fields :
			tmp[i] =  user[i]
		tmp['create_time'] = '%s' %(time.strftime("%Y %H:%M:%S"))
		#print tmp
		mes = addUser('users',tmp)
		print mes
		return render_template('mes.html',mes = mes ) 
	return render_template('adduser.html')


@app.route('/userlist')
def userlist():
	alluser = getUsers('users')
	return render_template('userlist.html',users = alluser)
'''
@app.route('/del')
def del():
	if request.method == "POST":
		u_id = request.form.get()	


@app.route('/update')
def update():
'''

if __name__ == "__main__":
	app.run(host='0.0.0.0' ,port=888,debug=True)
	

