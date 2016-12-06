#!/usr/bin/python
#coding:utf-8

from flask import Flask ,render_template,redirect,request
import MySQLdb as mysql
from datetime import datetime

datas = mysql.connect(user='root',passwd='123456',db='reboot',charset='utf8')
datas.autocommit(True)
cur = datas.cursor()

app = Flask(__name__)

def getNow():
	now = datetime.now().strptime("%Y-%m-%d %H:%M:%S")
	return now

@app.route('/user/userlist')
def userlist():
	fields = ["id","name","name_cn","password","email","mobile","role","status","create_time"]
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
		#cur.execute(d_sql)
		return redirect('/user/userlist')
	return render_template('test.html',errmes = d_sql)

if __name__ == "__main__":
	app.run(host='0.0.0.0',port=888,debug=True)
