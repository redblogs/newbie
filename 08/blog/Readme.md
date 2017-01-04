
# 1. login.html中如何使报错信息为红色(可以使用判断来过滤错误信息参数是否存在)

	<div style='color:red'>
		{{ mesmsg }}
	</div> 

# 2. 创建和删除session

	见login和loginout路由 

# 3.权限判断的话也是通过session实现

	session['role'] = 'admin'

# 4. v1_demo.py为version1版本，返回的主要为html页面

# 5. demo.py中登录页面实现jQuery实现，返回的为json字符串
