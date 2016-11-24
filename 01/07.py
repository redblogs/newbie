#__coding__:utf-8
year = raw_input("please  input year: ")

while year:
	if (int(year) % 400 == 0):
		print "run nian "
		break
	elif (int(year) % 100 != 0) and (int(year) % 4 == 0) :
		print "run nian "
		break
	else :
		year = raw_input("please  input year: ")
