from flask import Flask 

app = Flask(__name__)

@app.route('/')

def bai1():
	return "<h1> Hello World </h1>"

@app.route('/it')

def bai2():
	return "<h1> Chào mừng bạn đến với thế giới Backend của sinh viên năm 3 </h1>"

@app.route('/hello/<username>')

def bai3(username):
	return f"<h1> Xin chào {username} đã đến với website được tạo bằng Python/Flask </h1> "

if (__name__ == '__main__'):
	app.run(debug=True, port=5000)
