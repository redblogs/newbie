#coding:utf-8
arr = [1,3,65,2,6,32,0,7,14]

def sort_fn1(data):
	return data 

def sort_fn2(data):
	return data[1] 

def sort_fn3(data):
	return data['age'] 

def my_sort(arr,sort_fn1):
	for j in range(len(arr)-1):
		for i in range(len(arr)-1):
			if sort_fn1(arr[i]) >sort_fn1(arr[i+1]):
				arr[i],arr[i+1]=arr[i+1],arr[i]
	print arr


print my_sort(arr,sort_fn1)

arr2 = [('xiaohong',90),('xiaohua',58),('xiaohei',100)]
print my_sort(arr2,sort_fn2)

d = [{'name':'xiaohong','age':18},{'name':'xiaohei','age':10},{'name':'xiaowang','age':33}]
print my_sort(d,sort_fn3)

