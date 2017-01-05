import cookielib,urllib,urllib2

filename  = "cookie.txt"

cookie = cookielib.MozillaCookieJar(filename)

opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))

user = {'username':"liwei.fu","password":"qazQAZ!"}

testu = {"loginform-username":"XXXXXXXX","password":"XXXXX"}
postdata = urllib.urlencode(testu)

print postdata

loginurl = "http://home.51cto.com/index?reback=http://www.51cto.com/"

cookie.save(ignore_discard=True,ignore_expires=True)

testurl = "http://news.51cto.com/"
try:
	final = opener.open(testurl)
except urllib2.URLError,e:
	if hasattr(e,"code"):
		print e.code
	if hasattr(e,"reason"):
		print e.reason
else:
	print final.read()
