res = {'!': 1, '.': 1, 'Bob': 1, 'I': 2, 'a': 1, 'am': 2, 'boy': 1}

new = {}
for k ,v in res.items():
	new.setdefault(v,[])
	new[v].append(k)

print new
#keys = max(new)
#print "%s  ----> %s" %(keys,new[keys])

f = open('tongji.html',"w+")
str = "<table border='1px'><tr><th>times</th><th>word</th></tr>"
while True:
	keys = max(new)
	for i in new[keys]:
		str += "<tr><td>%s</td><td>%s</td></tr>" %(keys,i)
	new.pop(keys)
	if len(new) == 0 :
		break

str += "</table>\n"

f.write(str)

f.close()

