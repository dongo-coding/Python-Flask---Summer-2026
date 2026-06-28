from flask import Flask, request

app = Flask(__name__)

@app.route('/product/<int:product_id>')

def get_product(product_id):
	return f"<h3>Bạn đang xem sản phẩm có ID là {product_id} </h3>"

@app.route('/search')

def search_page():
	keyword = request.args.get('keyword', ' ')
	page = request.args.get('page', 1, type=int)
	return f"<h3>Kết quả tìm kiếm cho từ khóa: '{keyword}' (Trang số: {page})</h3>"
@app.route('/api/status')

def get_status():
	data = {
	"status": "success",
        "framework": "Flask",
        "streak": 2,
        "message": "Mọi thứ đang chạy rất mượt mà!"
	}
	return data

if __name__ == '__main__':
	app.run(debug=True, port=5000)
