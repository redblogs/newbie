#!/usr/bin/python
#coding:utf-8

from flask import Flask ,render_template,redirect,request,session
import MySQLdb as mysql
from datetime import datetime

datas = mysql.connect(user='root',passwd='123456',db='reboot',charset='utf8')
datas.autocommit(True)
cur = datas.cursor()


fields = ["id","name","name_cn","password","email","mobile","role","status","create_time"]

app = Flask(__name__)
#import session后初始化加密串
app.secret_key = "qazQAZ!@"

def getNow():
	now = datetime.now().strptime("%Y-%m-%d %H:%M:%S")
	return now


@app.route('/login',methods = ["GET","POST"])
def login():
	if request.method == "GET":
		return render_template("login.html")
	if request.method == "POST":
		login_user = dict( (k,v[0]) for k ,v in dict(request.form).items())
		tmp = ["name",'password']
		all_sql = "select %s from users " %','.join(tmp)
		cur.execute(all_sql)
		res = cur.fetchall()
		all_user = [ dict((v,row[k]) for k ,v in enumerate(tmp)) for row in res]
		#all_user==>[{'password': u'aa', 'name': u'KK'}, {'password': u'123456', 'name': u'TT'}, {'password': u'XX123as', 'name': u'XX'}, {'password': u'123as', 'name': u'Xman'}, {'password': u'123VV', 'name': u'AA'}]
		userName = [ x['name'] for x in all_user]
		if not login_user['name'] or not login_user['password']:
			errmsg = "Name or Password not Null"
			return render_template("login.html",result = errmsg)
		if  login_user['name'] not in userName:
                        errmsg = "Name is not exit"
                        return render_template("login.html",result = errmsg)
		else :

			password = [ x['password'] for x in all_user if x['name'] == login_user['name']][0]
			if  login_user['password'] != password:
        	                errmsg = "Password is not exist "
                	        return render_template("login.html",result = errmsg)
			#return render_template("login.html",result = 'login Success')
			else:
				session['name'] = login_user['name']
				return redirect('/user/userlist')
	

@app.route('/user/userlist')
def userlist():
	if not session.get('name',None):
		return redirect('/login')
	sql = "select %s from %s" %(','.join(fields),'users')	
	cur.execute(sql)
	res = cur.fetchall()
	users = [ dict((v,row[k]) for k ,v in enumerate(fields)) for row in res]
	return render_template('userlist.html',users = users)

@app.route('/user/delete')
def delete():
	if not session.get('name',None):
		return redirect('/login')
	id = request.args.get('id',None)
	print id
	d_sql = "No id error"
	if id :
		d_sql = "DELETE from users where id = %s" %  id
		cur.execute(d_sql)
		return redirect('/user/userlist')
	return render_template('test.html',errmes = d_sql)

@app.route('/user/update',methods=['GET','POST'])
def update():
	if not session.get('name',None):
		return redirect('/login')
	if request.method == "POST":
		user = dict(request.form)
		user = dict((k,v[0]) for k ,v in user.items())
		#print user ==>{'mobile': u'CCC', 'name_cn': u'ccccccc', 'id': u'2', 'name': u'cc', 'email': u'CC@chinacache.com'}
		#user.pop('id')
		tmp_list = [ "%s='%s'"%(k,v) for k,v  in user.items() if k != "id"]
		#print tmp_list
		update_sql = "UPDATE users set %s  where id=%s" %(','.join(tmp_list),user['id'])
		cur.execute(update_sql)
		return redirect('/user/userlist')
	else:
		id = request.args.get('id',None)
		print id
		select_sql = "No id error"
		if id :
			select_sql = "select %s from users  where id = %s" %(','.join(fields),id)
			print select_sql
			cur.execute(select_sql)
			res = cur.fetchone()
			#print res ==>(2L, u'cc', u'cc', u'cC23 ', u'CC@chinacache.com', u'CCC', u'user', 0, datetime.datetime(2016, 11, 30, 16, 4, 33))
			user = dict((v,res[k]) for k ,v in enumerate(fields))
			
			#return redirect('/user/userlist')
		return render_template('userinfo.html',user = user)

@app.route('/loginout')
def loginout():
	session.pop('name')
	return redirect('/login')

if __name__ == "__main__":
	app.run(host='0.0.0.0',port=888,debug=True)
