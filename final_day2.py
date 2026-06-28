from flask import Flask

app = Flask(__name__)

@app.route('/api/user/<int:user_id>')
def check(user_id):
  if user_id>0 and user_id<100:
    return {"id" : user_id, "name" : Do Ngo, "role" : "Student"}
  else:
    return {"error" : "User not found","status" : 404}

if __name__ == '__main__':
    app.run(debug=True,port=5000)
    
      
