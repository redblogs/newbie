#/usr/bin/python
#coding:utf-8

def htmlStr(arr):
        html_str = "<html><h4>/usr/local/src/newbie/04/ketang/test.py ====>result[test.html]<h4>\n<table border='1px'>\n<tr><th>%s</th><th>%s</th><th>%s</th></tr>\n" %('Count','IP','URL')
        for i in arr:
                html_str += "<tr><td>%s</td><td>%s</td><td>%s</td></tr>\n" %(i[1],i[0][0],i[0][1])

        html_str += "</table></html>\n"
        return html_str

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

test = operateFile('log.log')
test = test[:10]
htmlstr = htmlStr(test)

print operateFile('/var/www/html/test.html',mode='w',string=htmlstr)
