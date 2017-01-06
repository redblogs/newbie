#!/usr/bin/python
#coding:utf-8

import MySQLdb as mysql 

conn = mysql.connect(user='root',passwd='123456',db='reboot',charset='utf8')
cur = conn.cursor()
conn.autocommit(True)
#datas = mysql.connect(user='root',passwd='123456',db='reboot',charset='utf8')
#datas.autocommit(True)
#cur = datas.cursor()

def getById(id):
	fields = ['id','name','name_cn','mobile','email']
	sql = "select %s from users WHERE id = '%s'" %(','.join(fields),id)
	#print sql
	cur.execute(sql)
	res = cur.fetchone()
	if res :
		user = dict((v,res[k]) for k ,v in enumerate(fields) )
		return user
	else :
		errmsg = "id is not exist "
		return errmsg 
if __name__ == "__main__":
	print getById(1)
