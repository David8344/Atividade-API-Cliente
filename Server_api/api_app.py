from flask import Flask, .
from jsons.data import *
  

app = Flask(__name__)
app.debug = True



@app.route('/')
def index():
  #retorne a lista de users vindo do arquivo data.py
  return jsonify(users)

@app.route('/users/<int:user_id>')
def users(user_id):
    return users[user_id+1]
    
app.run(debug=True, port=5000)
