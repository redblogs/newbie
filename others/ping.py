#/usr/local/python
#coding:utf-8
##定义ping的函数,参数有前三段ip段,第四段ip的起始,以及需要的ip个数
 

import os ##调用os.system()执行ping命令
def batchPing(head='192.168.137',start=0,end=12,num = 10):
	tmp = [] 
	#count = 0
	for i in range(start,end+1):
		#count += 1	
		#ip_str = 'ping -c 10' +head + '.' + str(i) 
		ip_str = "%s %s.%s %s" %('ping -c 10 -i 0.2 -w 3',head,str(i),'&> /home/ipresult.txt') 
		#print "di %s ci : %s" %(count,ip_str)
		##执行ping命令
		res = os.system(ip_str)
		if res  != 0:
			tmp.append(ip_str)
	return tmp[:num]

##将上述整理的ip写入到文件中去			
def operateFile(tmp=[]):
	with open('/home/useableIp.txt','w') as files:
		for i in tmp:
			#i = i.strip('&> /home/ipresult.txt')
			i = i.split(' ')[7]
			files.write('%s\n' %i)
	return "Done"
	
	
if __name__ == "__main__":
	linshi =  batchPing(head='112.90.148',start=237,end=254,num = 64)
	print operateFile(linshi)
