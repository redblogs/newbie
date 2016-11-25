arr = [1,3,65,2,6,32,0,7,14]

def sort_fn1(data):
        return data

def sort_fn2(data):
        return data[1]

def sort_fn3(data):
        return data['age']

print sorted(arr,key=sort_fn1)

arr2 = [('xiaohong',90),('xiaohua',58),('xiaohei',100)]
print sorted(arr2,key=sort_fn2)
d = [{'name':'xiaohong','age':18},{'name':'xiaohei','age':10},{'name':'xiaowang','age':33}]
print sorted(d,key=sort_fn3)
