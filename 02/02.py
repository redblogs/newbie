#arr = [1,3,5,8,11,23,27,55,100,104,123,155,200,320,333,555]
#arr = [1,3,5,8,11]
arr = range(100)
x = raw_input("qing shuru yi ge shuzi ")
start = 0 
end = len(arr)-1
count = 0 
while True :
	count += 1 
	half = ( start + end )/2
	if int(x) > arr[half]:
		start = half
	elif int(x) < arr[half]:
		end = half
	else :
		print "The index value is %s" %half 
		break 

print "Total found  %s times " %count
