# 1. 将login.html扒取jumpServer 界面
	
	*使用ajax实现登录功能

# 2.登录思路

	* 登录验证成功，将name存入session['name'],用于在跳转到userinfo.html个人页面时获取用户信息

	* ajax实现异步渲染userinfo.html页面,拼接tbody字段的html内容，计划将实现更新按钮的ajax请求功能实现

	* 此html页面处需要使用两个ajax

	** 1.ajax实现html中tbody的拼接

	** 2. ajax实现更新的按钮事件监听，点击更新按钮跳转个人的更新页面
