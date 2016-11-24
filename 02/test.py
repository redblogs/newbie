def InsertSort(mylist):  
    size = len(mylist)  
    i = 1  
    for i in range(1, size):  
	print "===================================di %s ci xun huan ======================="  % i
	print "mylist[i]=== mylist[i-1] : %s == %s"  %(mylist[i],mylist[i-1])
        if mylist[i] < mylist[i - 1]:  
            tmp = mylist[i]  
            j = i - 1  
	    print "****j : %s" %j
            mylist[j + 1] = mylist[j]  
              
            j = j - 1  
            while j >= 0 and mylist[j] > tmp:  
                 mylist[j + 1] = mylist[j]  
                 j = j - 1  
            mylist[j + 1] = tmp        
#mylist0 = [12, 11, 13, 1, 2, 4, 3]  
mylist0 = [6 , 5 , 3 , 1 , 8 , 7 , 2 , 4]
InsertSort(mylist0)  
print(mylist0)
