##04节课的作业,用文件实现登录注册功能


*作业要求 ：(函数思路去改造,作业。思路)

	1.复习上次作业和课堂内容

	2.让用户输入用户名,然后输入密码
		
		登录失败(每经过验证),继续提示用户密码不匹配

		登录成功之后,提示登录成功消息


*注册： 1.让用户输入用户名,让后输入密码

	2.如果用户名重复,提示错误消息,注册失败

	3.如果用户名不重复,提示注册成功。

	4.持久化(程序关闭后再次执行仍然可以读取,用户名仍可以使用)

* 函数中return值可以根据情况进行调整：

		In [6]: def hello(string):
		   ...:     if string in 'hello':
		   ...:         print string
		   ...:         return 'True'
		   ...:     else :
		   ...:         print 'Not in '
		   ...:         return 'False'
		   ...:         
		   ...:       
		   ...:     

		In [7]: t = hello('h')
		h

		In [8]: print t 
		True

		In [9]: t = hello('s')
		Not in 

		In [10]: print t 
		False

* 函数中return值可以放在break前边:

		In [15]: def phone(tmp = 5):
			...:     while True:
			...:         print "The values of tmp is %s " %tmp 
			...:         tmp -= 1
			...:         if tmp == 2 :
			...:             print tmp
			...:             return tmp
			...:             break
			...:     

		In [17]: t = phone()
		The values of tmp is 5 
		The values of tmp is 4 
		The values of tmp is 3 
		2

		In [18]: print t 
		2

		In [19]: 

* 函数参数中如果需要传递的参数为函数时,前边要先放参数为函数,然后再是其他参数

		具体代码见zhuce.py文件中zhuce(wirteFile,tmp = user)的调用
