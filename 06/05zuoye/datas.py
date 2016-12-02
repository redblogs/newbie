def getUsers(filename):
	with open(filename) as f:
		arr =[line.split(':') for line in  f.read().split('\n') if line != '']
		#print arr
		res = dict((x[0],x[1]) for x in arr )
	return res
def updateFile(filename,mode ,*tmp):
	with open(filename,mode) as f:
		f.write("%s:%s\n" %tmp)
	return "update ok"

if __name__ == '__main__':
	print  getUsers('users.txt')
