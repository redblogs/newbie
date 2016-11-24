arr = [3 , 5, 1 ,32 , 4]
print "The   sorted  arr  is   : %s" % arr

l = len(arr)
print l 
for i in range( l-1 ):
	print "di  %s ci xuanze paixu " %i 
	#jiang a[i] qu chu lai  fen bie yu  houbian bijiao 
	for j in range(i+1,l):
		if arr[i] > arr[j]:
			arr[i] ,arr[j] = arr[j],arr[i]
	print arr
	
print "*" * 40
print arr
