#coding:utf-8
import sys
f = open('users.txt')
tlist = []
num = 1 
while True:
	line = f.readline()
	print repr(line)  #打印原始的数据
	print "%s --> %s" %(num,line.strip("\n"))
	tmp = line.strip('\n').split(":")
	tlist.append(tmp)
	num += 1 
	if len(line) == 0:
		print tlist
		break;

##字典生成式将其转换为用户名:密码的字典数据格式
res = dict((x[0],x[1]) for x in tlist if x != [''])
print res

while True :
    name = raw_input("Please input The username : ")
    if name not in res.keys():
        print "The user is not exists"
        sys.exit(6)
    time = 1
    while time < 4:
        pword = raw_input("Please input the password %s times :" %time)

        if ( len(pword) == 0 ) or pword != res[name]:
            print "The password is Wrong"
        else:
            print "login Sucess"
            sys.exit(0)
        if time == 3:
	    print "不好意思,密码输入次数过多,账户已经锁定，请联系管理员"
            sys.exit(1)
        time += 1
