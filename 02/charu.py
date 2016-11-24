arr = [6 , 5 , 3 , 1 , 8 ]#, 7 , 2 , 4]
sorted_arr = []

def charu():
	
print "The origin arr is : %s " %arr
l = len(arr)

for i in range(l):
        if i != 0 :
                sorted_l = len(sorted_arr)
                print sorted_l
                for time in range(sorted_l,0,-1):
                        if arr[i] > sorted_arr[time-1]:
                                sorted_arr.append(arr[i])
                                #sorted_arr.insert(time-1,arr[i])
                        elif arr[i] < sorted_arr[0]:
				sorted_arr.insert(0,arr[i])
			else :
				pass


        else :
                sorted_arr.append(arr[i])



print sorted_arr
