<html>
<head>
<meta charset='utf-8'>
<title>login</title>
</head>
<body>
<table>
	<!--<form action='/login' method="POST">-->
	<form id="loginForm">
	<tr><td>Name<input id ="name"  type='text' name='name'> </td></tr>
	<tr><td>Password<input id ="password" type='password' name='password'> </td></tr>
	<tr><td><input id ="loginbtn" type='submit' value='login'></td></tr>
	</form>
</table>
<script src='/static/js/jquery-3.1.0.min.js'></script>
<script>
//#注释使用两个斜杠'//'
//alert('welcome jquery')
$('#loginbtn').on('click',function(){
	var str = $('#loginForm').serialize()
	$.post('/login',str,function(data){
		data = JSON.parse(data)
		if (data['code'] == 0){
			location.href='/userlist'
		}else{
			$('#errmsg').html(data['errmsg'])
		}
	})
	return false
})
</script>
</body>
</html>
