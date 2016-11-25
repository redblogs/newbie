arr = [1,3,2,78,21,32,55,0,9]

arr2 = [('xiaohong',90),('xiaohua',58),('xiaohei',100)]

d = [{'name':'xiaohong','age':18},{'name':'xiaohei','age':10},{'name':'xiaowang','age':33}]
print sorted(arr,key=lambda x:x)

print sorted(arr2,key=lambda x:x[1])

print sorted(d,key=lambda x:x['age'])
