#!/usr/bin/python
#coding:utf-8

from flask import Flask ,render_template,request



app = Flask(__name__)

@app.route('/test' ,methods=['GET','POST'])
def test():
	if request.method == "POST":
		#sex = request.form.get('sex','')
		print dict(request.form)
	return render_template('test.html')



if __name__ == "__main__":
	app.run(host='0.0.0.0',port=888,debug=True)
