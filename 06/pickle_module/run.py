#/usr/bin/python
#coding:utf-8

from flask import Flask ,request,redirect,render_template
from datas import *
app = Flask(__name__)

def index():
	return "Please login "

@app.route('/')
@app.route('/login',methods=['GET','POST'])
def login():
	if request.method == 'POST':
		print request.method
		name = request.form.get('name','')
		password = request.form.get('password','')
		arr = request.form
		print "*" * 40 
		print name ,password ,arr
		print "*" * 40 
		#tmp = dict((x[0],x[1]) for x in arr)
		users =getUsers('users.txt')
		if (not name) or (name not in users):
			errmsg = "name wrong"
			return render_template('login.html',errmsg=errmsg)
		else :
			if (not password ) or (password != users[name]):
				errmsg =  "password wrong"
				return render_template('login.html',errmsg=errmsg)
			else:
				mes =  "login Success"
				return redirect('/userlist')
	return render_template('login.html')

@app.route('/userlist')
def userlist():
	tmp = getUsers('users.txt')
	#print tmp
	errmsg = ''
	return render_template('userlist.html',arr = tmp,msg = errmsg)

@app.route('/adduser')
def adduser():
	name = request.args.get('name','')
	password = request.args.get('password','')
	tmp = getUsers('users.txt')
	if (not name) or (name  in tmp):
		errmsg = "name wrong"
		return render_template('adduser.html',arr = tmp ,msg=errmsg)
	if (not password ) :
		errmsg = "password wrong"
		return render_template('adduser.html',arr = tmp ,msg=errmsg)
	updateFile('users.txt','a+',name,password)
	errmsg = "Adduser sucess"
	tmp[name] = password
	return render_template('adduser.html',arr = tmp ,msg=errmsg)
		

@app.route('/del')
def delete():
	delname = request.args.get('delname','')
	print delname
	tmp = getUsers('users.txt')
	if delname in tmp:
		tmp.pop(delname)
		#以w模式清空下文件,以免重写文件出现覆盖现象
		tmpf = open('users.txt','w')
		tmpf.close()
		for x in tmp.items():
			print x
			updateFile('users.txt','a+', x[0],x[1])
		errmsg = "Delete success"
		return render_template("userlist.html",arr = tmp ,msg = errmsg)
	else :
		errmsg = "The remove name is not exists"
		return render_template("userlist.html",arr = tmp ,msg = errmsg)

if __name__ == "__main__":
	app.run(host='0.0.0.0',port=888,debug=True)

