##通过datas.py文件简单实现自己给数据然后通过函数来更改数据库内的数据。

##具体代码见datas.py文件中的函数

*个人心得体会：

	*插入新增数据和更改数据的格式是不同的

	新增数据我使用了元组来直接将列表转换，sql = "insert into %s(%s) values %s" %(tbName,','.join(fields),tuple([user[x] for x in fields]))

	更改数据基本都是通过id号来更改的sql = 'update %s set %s where id="%s"' %(tbName,','.join(tmp),u_id)
	
	删除数据也是通过id号来删除的 sql = "DELETE FROM %s where id='%s'" %(tbName,u_id)
##run.py为程序的执行入口
