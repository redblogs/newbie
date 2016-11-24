arr = [33,3 , 5, 1 ,32 , 4]
print arr
length = len(arr)
print length
for j in range(length-1):
	print "di %s ci xun huan :" %j
	for i in range(length-1-j):
		if arr[i] > arr[i+1]:
			arr[i],arr[i+1] = arr[i+1],arr[i]
	print arr



print "The final result is %s" % arr
