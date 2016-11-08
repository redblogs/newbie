#/usr/bin/python
import sys
from  zhuce  import wirteFile


def readUser(filename,type = 'dict'):
	tmp = []
	if type == 'list':
		with open(filename) as readf:
			for i in readf:
				line = i.strip('\n')
				tmp.append(line)
		return tmp
	else:
		with open(filename) as readf:
			for i in readf:
				#print repr(i) 
				line = i.strip('\n').split(':')
				tmp.append(line)
		res = dict((x[0],x[1]) for x in tmp)
		return  res

####login Module
def login():
	while True :
		name = raw_input("Please input The username : ")
		res = readUser('users.txt')
		lockuser = readUser('lockUser.txt',type = 'list')
		lockuser = [ x for x in lockuser if x != '' ]
		print "lockuser is %s " % lockuser
		if name not in res.keys():
			print "The user is not exists"
			sys.exit(6)
		if name in lockuser:
			print "The user is locked ,please contact administrator"
			sys.exit(7)
		time = 1
		while time < 4:
			pword = raw_input("Please input the password %s times :" %time)
			if ( len(pword) == 0 ) or pword != res[name]:
				print "The password is Wrong"
			if pword == res[name]:
				print "login Sucess"
				sys.exit(0)
			if time == 3:
				wirteFile('lockUser.txt',name)
				print name
				sys.exit("The user ID locked ,please connact administrator.")
			time += 1


if __name__ == '__main__':
	login()


