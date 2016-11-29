def readUser(filename,type = 'dict'):
	tmp = []
        with open(filename) as readf:
        	for i in readf:
        	#print repr(i) 
        		line = i.strip('\n').split(':')
        		tmp.append(line)
        res = dict((x[0],x[1]) for x in tmp)
        return  res


if __name__ == '__main__':
	readUser('users')
