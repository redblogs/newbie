d = {'10.35.1.82': 61, '101.227.4.33': 2, '111.85.41.230': 103,'218.200.66.196': 14,'218.200.66.197': 21,'218.200.66.198': 25,'218.200.66.199': 19,'220.172.215.69': 1,'220.181.125.177': 1,'221.176.5.153': 31,'221.176.5.154': 3,'221.176.5.156': 3}

tmp = d.items()
print tmp
le = len(tmp)
for i in range(le-1):
	for j in range(le-1-i):
		if tmp[j][1] < tmp[j+1][1]:
			tmp[j],tmp[j+1] = tmp[j+1],tmp[j]


print "sorted tmp :%s" %tmp

tmp = tmp[:3]
for i in tmp:
	print "ip is %s ,count is %s" %i 
