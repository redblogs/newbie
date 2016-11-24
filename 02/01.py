store = []
while True:
	x = raw_input("qing shu ru action: ")
	if x == "add":
		y = raw_input("qing shu ru thing: ")
		store.append(y)
		print store
	elif x == "do":
		print "****do "
		print len(store)
		if len(store) != 0:
			print store.pop()
		else:
			print "nothing"
	else :
		
		print "The final result is %s" %store
		break
