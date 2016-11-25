#coding:utf-8
def operate_file(filename):
	res = {}
	with open(filename) as f:
		for line in f:
			ip = line.strip('\n')
			ip = ip.split(" ")[0]
		#	print ip
			res[ip] = res.get(ip,0)+1
		return sorted(res.items(),key=lambda x:x[1],reverse=True)

tmp =  operate_file("log.log")
tmp = tmp[:10]
print tmp
def op_file(filename,mode='r',tmp):
        f = open(filename,mode)
        str = "/usr/local/src/newbie/04/sorted==>result\n<table border='1px'><tr><th>times</th><th>word</th></tr>"
        while True:
                for i in tmp :
                        str += "<tr><td>%s</td><td>%s</td></tr>" %i
                if len(new) == 0 :
                        break

        str += "</table>\n"
        if ('w' in mode) or ('a' in mode) :             ##使用in来判断模式是否为写模式
                f.write(str)

        f.close()
op_file(filename='/var/www/html/nginxlog.html',mode="w+",tmp)
