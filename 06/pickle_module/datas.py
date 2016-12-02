#/usr/local/python
#coding:utf-8
'''
	##使用pickle实现对users.txt文件中用户密码的增、删、改、查功能
'''
from  pickle import dump ,load

#定义全局变量filename,用于测试
filename = 'users.txt'


#获取所有用户名密码,从filename文件中读取
def getUsers():
	with open(filename,'rb') as readf:
		res = load(readf)
	return res

#添加用户
def addUser(name,password):
	tmp = getUsers()
	if  (not name) or (not password):
		errmsg = "Wrong name or password"
		return errmsg 
	if (name in tmp):
		errmsg = "name is exists"
		return errmsg 
	tmp[name] = password
	msg =  "%s:%s ---->adding" %(name,password)
	with open(filename,'wb') as updatef:
		dump(tmp,updatef)
	return msg 

##更改用户
def updateUser(name,password):
	tmp = getUsers()
	if name not in tmp:
		errmsg = 'The update username is not exist'
		return errmsg
	msg =  "Update  %s:%s ---->%s" %(tmp[name],password,name)
	tmp[name] = password
        with open(filename,'wb') as updatef:
                dump(tmp,updatef)
        return msg

#删除用户
def deleteUser(name):
	tmp = getUsers()
	if name not in tmp:
		errmsg = 'The delete username is not exist'
		return errmsg
	msg =  "Delete  %s ---->%s" %('users.txt',name)
	tmp.pop(name)
        with open(filename,'wb') as updatef:
                dump(tmp,updatef)
        return msg

##查找用户名对应的密码
def findUser(name):
	tmp = getUsers()
	if name not in tmp :
		errmsg = "The username is not exists"
		return errmsg
	return tmp[name]

##主程序入口
if __name__ == "__main__":
	print getUsers()
	print findUser('')
	print findUser('AA')
	print "add user %s" % ('*' * 40)
	print addUser('pc','pc123')
	print addUser('TT','')
	print addUser('','pc123')
	print addUser('AA','pc123')
	print "update user %s" % ('*' * 40)
	print updateUser('AA1','123')
	print updateUser('AA','AA123')
	print "delete user %s" % ('*' * 40)
	print deleteUser('AA1')
	print deleteUser('pc')
