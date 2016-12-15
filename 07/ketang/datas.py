#/usr/bin/python
#coding:utf-8

import MySQLdb as mysql
import datetime 

'''
这个文件基本实现了数据库的增删改查等操作,并且实验已经成功。
接下来需要结合前端的html页面通过post和get方法来融合实现前后端交互。
	以完成数据的增删改查。
'''




##获取数据库中所有的用户数据
def getUsers(tbName):
	db = mysql.connect(user='root',passwd='123456',host='127.0.0.1' ,db='reboot',charset='utf8')
	cur =  db.cursor()
	fields = ['id' ,'name' , 'name_cn','email','mobile','status','role','create_time']
	sql = 'select %s from %s' %(','.join(fields),tbName)
	#print sql
	cur.execute(sql)
	res = cur.fetchall()
	users = [ dict((v,row[k]) for k ,v in enumerate(fields)) for row in res]
	#for row in res :
	#	user = {}
	#	for k ,v in enumerate(fields):
	#		user[v] = row[k]
	#	users.append(user)
	return users

##查询指定用户的所有数据

def getOne(tbName,u_id):
	db = mysql.connect(user='root',passwd='123456',host='127.0.0.1' ,db='reboot',charset='utf8')
	cur =  db.cursor()
	user = {}
	fields = ['id' ,'name' , 'name_cn','email','mobile','role','status','password']
	sql = "select %s from %s where id='%s' " %(','.join(fields),tbName,u_id)
	#查询name存在,tmp=1;不存在,tmp=0
	tmp = cur.execute(sql)
	#name存在的情况下执行,即tmp=1 
	if tmp:
		res = cur.fetchone()
		#字典生成式代替简单的for遍历赋值
		user = dict((v,res[k]) for k ,v in enumerate(fields))
		#for  k ,v in enumerate(fields):
		#	user[v] = res[k]
		return user
	return "The select user is not exists"

##改,参数中user为字典
def updateMes(tbName,user):
	db = mysql.connect(user='root',passwd='123456',host='127.0.0.1' ,db='reboot',charset='utf8')
	cur =  db.cursor()
	#user = {'mobile': '1324134', 'email': 'RR@china.com', 'name_cn': 'RR', 'id': '1', 'name': 'RR'}
	tmp = []
	u_id = user['id']
	user.pop("id")
	for k ,v in user.items():
		tmp.append("%s='%s'" %(k,v))
	sql = 'update %s set %s where id="%s"' %(tbName,','.join(tmp),u_id)
	print sql
	cur.execute(sql)
	db.commit()
	cur.close()
	db.close()
	return "update OK"

##增,参数中user为字典
#user = {'name':'Xman','name_cn':'Xman','password':'123as','email':'Xman@chinacache.com','mobile':'123213','role':'user','status':0,'create_time':'%s' %(time.strftime("%Y %H:%M:%S"))}
def addUser(tbName,user):
	db = mysql.connect(user='root',passwd='123456',host='127.0.0.1' ,db='reboot',charset='utf8')
	cur =  db.cursor()
	#insert 语句模板 "insert into users(name,name_cn,password,email,mobile,role,status,create_time) values ('ss','ss','ss123 ','ss@chinacache.com','ssss','user','0','%s') " %(time.strftime("%Y %H:%M:%S"))
	#利用元素直接格式化字符串,用来新增一条数据
	fields = ['name','name_cn','password','email','mobile','role','status','create_time']
	sql = "insert into %s(%s) values %s" %(tbName,','.join(fields),tuple([user[x] for x in fields]))
	print sql 
	#获取所有用户
	alluser = getUsers('users')
	#print alluser
	#用来存放存在用户名的列表,tmp = [u'KK', u'TT', u'ss', u'XX']
	tmp = [one['name'] for one in alluser]
	if user['name'] not in tmp:
        	cur.execute(sql)
        	db.commit()
        	cur.close()
        	db.close()
        	return "Insert  OK"
	return "has exists"
	


##删,判断删除的数据是否存在;存在则删除,不存在则返回报错
#eg:delete from users where id=3;
def delUser(tbName,u_id):
	db = mysql.connect(user='root',passwd='123456',host='127.0.0.1' ,db='reboot',charset='utf8')
	cur =  db.cursor()
	sql = "DELETE FROM %s where id='%s'" %(tbName,u_id)
        #print sql
        res = cur.execute(sql)
	if res:
        	db.commit()
      		cur.close()
        	db.close()
        	return "Delete  OK"
	return "The id is not exist"
#更改密码的函数,线上业务都是将密码单独出来的
def modifyPasswd(tbName,temp):
	##temp = {'newpassword': 'aa', 'oldpassword': 'aa', 'id': '1'}
	temp['id'] = int(temp['id'])
	print temp
	db = mysql.connect(user='root',passwd='123456',host='127.0.0.1' ,db='reboot',charset='utf8')
	cur =  db.cursor()
	alluser = getUsers('users') 
	user = getOne('users',temp['id'])
	tmp = [ x['id'] for x in alluser ]
	print "tmp " *5 
	print tmp
	if temp['id'] not in tmp:
		errmsg = "The user is not exist"
		return errmsg
	if (not temp['newpassword']) or ( temp['oldpassword'] !=  user['password']):
		errmsg = "Oldpassword Wrong! "
		return errmsg
	sql = "update %s set password = '%s' where id = %s" %(tbName,temp['newpassword'],temp['id'])
	print sql
	cur.execute(sql)
	db.commit()
	cur.close()
	db.close()
	return "Change Password  Success"

if  __name__ == "__main__":
	print getOne('users',2)
