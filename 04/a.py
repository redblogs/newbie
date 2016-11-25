num = 3

def hello():
	global num 
	num = 5
	print num


print hello()
print "num = %s" %num
