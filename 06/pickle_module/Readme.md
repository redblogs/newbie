##使用pickle模块实现存取文件,便于直接将用户名、密码的字典直接存放到文件中,需要时直接取出来使用就行。



##知识点import pickle

##*pickle.dump(dict,filename) ##将字典写入文件,注意操作时需要提前打开文件,pickle为二进制的写入,f = open(filename,'wb')

##*pickle.load(filename)  ##将文件中二进制的内容读取出来.

##datas.py 简单的实现了用户的增删改查功能,可以考虑结合flask实现较为优雅的数据存放.不过重点还是flask结合数据库的使用.
