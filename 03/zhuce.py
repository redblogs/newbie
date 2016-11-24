f = open("users.txt","a+")

#f.write("wd:123\n")
#mes = ["kk:321\n","ss:456\n"]
#f.writelines(mes)
while True:
	name = raw_input("Please input you name :").rstrip()
	passwd = raw_input("Please input you password: ")
	repass = raw_input("Please confirm you password: ")
	if len(name) == 0:
		print "Name can't NULL,Input name again"
		continue
	if( passwd != repass) or (len(passwd) == 0) or (len(repass) == 0):
		print "Password Wrong"
	else :
		tmp = ["%s:%s\n" %(name,passwd)]
		f.writelines(tmp)
		#print "tmp is %s" %tmp
		print " OK "
		break


f.close()
