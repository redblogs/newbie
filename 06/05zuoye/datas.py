def getUsers(filename):
	with open(filename) as f:
		arr =[line.split(':') for line in  f.read().split('\n') if line != '']
		#print arr
		res = dict((x[0],x[1]) for x in arr )
		return res


if __name__ == '__main__':
	result = getUsers("users.txt")
	print result
