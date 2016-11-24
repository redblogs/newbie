#/usr/bin/python
import sys
f = open('users.txt','r')
tlist = []
for i in f.readlines():
    print i.strip('\n')
    t = i.strip('\n').split(":")
    tlist.append(t)


print tlist
res = dict((x[0],x[1]) for x in tlist)
print res
f.close()
####login Module
while True :
    name = raw_input("Please input The username : ")
    if name not in res.keys():
        print "The user is not exists"
        sys.exit(6)
    time = 1
    while time < 4:
        pword = raw_input("Please input the password %s times :" %time)

        if ( len(pword) == 0 ) or pword != res[name]:
            print "The password is Wrong"
        else:
            print "login Sucess"
            sys.exit(0)
        if time == 3:
            sys.exit(1)
        time += 1

