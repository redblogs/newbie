#/usr/bin/python
#coding:utf-8


##第一步:分析日志,统计出url、ip对应出现的次数
def operateFile():
	res = {}
	with open('log.log') as files:
		for line in files:
			#print line 
			line = line.strip('\n').split(' ')
			#print line
			tmp = (line[0],line[6])#,line[8])
			res[tmp] = res.get(tmp,0)+1
			#print "res is %s" %res
		return sorted(res.items(),key=lambda x:x[1],reverse = True)



###第二步,将上述排好序的列表元素写入到html页面中去

##可以分成两部分,一:拼接写入html网页的str语句
##		 二:打开文件将拼接的str语句写入到文件中去

'''
arr = [(('61.159.140.123', '/favicon.ico'), 11), (('208.115.111.74', '/robots.txt'), 3), (('113.95.36.30', '/favicon.ico'), 3), (('124.31.124.140', '/public/js/tbox/box.js?20110824'), 2), (('171.106.90.131', '/public/js/xheditor/xheditor-1.1.12-zh-cn.min.js'), 2), (('111.85.41.230', '/data/uploads/2014/0801/11/small_53db0520523aa.jpg'), 2), (('124.31.124.140', '/public/js/jquery.jgrow.min.js'), 2), (('124.31.124.140', '/public/js/scrolltopcontrol.js?20110824'), 2), (('218.200.66.201', '/data/uploads/2014/0529/11/small_5386a98b393ac.jpg'), 2), (('111.85.41.230', '/data/uploads/2014/0801/11/small_53db0525e3c0a.jpg'), 2)]
'''
##拼接写入html网页的str语句
def htmlStr(arr):
	html_str = "<html><h4>/usr/local/src/newbie/04/ketang/run.py ====>result[nginx.html]<h4>\n<table border='1px'>\n<tr><th>%s</th><th>%s</th><th>%s</th></tr>\n" %('Count','IP','URL')
	for i in arr:
		html_str += "<tr><td>%s</td><td>%s</td><td>%s</td></tr>\n" %(i[1],i[0][0],i[0][1])
	
	html_str += "</table></html>\n"
	return html_str


##打开文件将拼接的str语句写入到文件中去
'''
》》由于文件的读、写只是mode的不同
'''
def writeHtml(filename,string):
	with open(filename,'w') as files:
		files.write(string)
	return 'Write OK'
'''
>>>>>>>>>>  Vertion 2  合并两次文件的读写(合并函数验证成功,具体见test.py文件) <<<<<<<<<<<<<<<<<<<<<<<
def operateFile(filename,mode='r',string=''):
	if ('w' in mode) or ('a' in mode):
		with open(filename,'w') as files:
			files.write(string)
		return 'Write OK'
	else:
		res = {}
		with open(filename) as files:
			for line in files:
				#print line 
				line = line.strip('\n').split(' ')
				#print line
				tmp = (line[0],line[6])#,line[8])
				res[tmp] = res.get(tmp,0)+1
				#print "res is %s" %res
			return sorted(res.items(),key=lambda x:x[1],reverse = True)
		
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
'''

if __name__ == "__main__":
	test = operateFile()
	test = test[:10]
	#print test
	htmlstr = htmlStr(test)
	#print htmlstr
	print writeHtml("/var/www/html/nginx.html",htmlstr)

	


