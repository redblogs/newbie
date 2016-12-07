#!/usr/bin/python
#coding:utf-8

from flask import Flask ,render_template,redirect,request
import MySQLdb as mysql
from datetime import datetime

datas = mysql.connect(user='root',passwd='123456',db='reboot',charset='utf8')
datas.autocommit(True)
cur = datas.cursor()


fields = ["id","name","name_cn","password","email","mobile","role","status","create_time"]

app = Flask(__name__)

def getNow():
	now = datetime.now().strptime("%Y-%m-%d %H:%M:%S")
	return now

@app.route('/user/userlist')
def userlist():
	sql = "select %s from %s" %(','.join(fields),'users')	
	cur.execute(sql)
	res = cur.fetchall()
	users = [ dict((v,row[k]) for k ,v in enumerate(fields)) for row in res]
	return render_template('userlist.html',users = users)

@app.route('/user/delete')
def delete():
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


if __name__ == "__main__":
	app.run(host='0.0.0.0',port=888,debug=True)
