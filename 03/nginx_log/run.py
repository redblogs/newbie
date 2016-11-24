#/usr/bin/python 
#coding:utf-8

##统计ip以及其对应出现的次数
res = {}
with open('log.log') as f:
	for line in f:
		ip = line.strip('\n')
		ip = ip.split(" ")[0]
		print ip
		res[ip] = res.get(ip,0)+1
#print res 


###panda的方法:翻转字典,以出现数字为key,出现ip统计到列表中去
#new = {}
#
#for k ,v in res.items():
#	new.setdefault(v,[])
#	new[v].append(k)
#
#print new


####woniu的方法
###将res字典转换为list后排序
tmp = res.items()
print tmp

