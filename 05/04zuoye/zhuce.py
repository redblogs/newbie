#/usr/bin/python 
#coding:utf-8

def wirteFile(filename,tmp):
	with open(filename,'a+') as writef:
		writef.writelines(tmp)
	return " 注 册 成 功 "

def readUser(filename):
	tmp = []
	with open(filename) as readf:
		for i in readf:
			#print repr(i) 
			line = i.strip('\n').split(':')
			tmp.append(line)
	res = dict((x[0],x[1]) for x in tmp)
	return  res

def zhuce(fn ,tmp = {}):
	while True:
		name = raw_input("Please input you name :").rstrip()
		passwd = raw_input("Please input you password: ")
		repass = raw_input("Please confirm you password: ")
		if len(name) == 0:
			print "Name can't NULL,Input name again"
			continue
		if name in tmp:
			print "Name is exist,Input name again"
			continue
		if( passwd != repass) or (len(passwd) == 0) or (len(repass) == 0):
			print "Password Wrong"
		else :
			tmp = "%s:%s\n" %(name,passwd)
			print fn('users.txt',tmp)
			break
'''
	#print 'tmp is %s' %tmp
	#f.write("wd:123\n")
	#mes = ["kk:321\n","ss:456\n"]
	#f.writelines(mes)
'''

if __name__ == '__main__':
	user = readUser('users.txt')
	#print user  #print调试大法,通过print打印来排查错误
	zhuce(wirteFile,tmp = user)
