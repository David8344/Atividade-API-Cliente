from flask import Flask, jsonify
import json


  

  

app = Flask(__name__)
app.debug = True
#carregue o arquivo todos.json e salve na variável todos_obj
todos_obj = json.load(open('todos.json'))
#carregue o arquivo users.json e salve na variável users_obj
users_obj = json.load(open('users.json'))

@app.route('/')
def index():
    
    #retorne a variável todos_obj
    return todos_obj

@app.route('/todos')
def todos():
    #retorne a variável todos_obj
    return todos_obj
    
@app.route('/users')
def users():
    
    #retorne a variável users_obj
    return users_obj



@app.route('/users/<int:user_id>')
def user(user_id):
    return users_obj[user_id-1]

@app.route("/users/<int:userid>/todos")
def usertodos(userid):
    #crie uma lista vazia chamada user_todos
    user_todos = []
    #percorra todos os itens da lista todos_obj
    for todo in todos_obj:
        #se o id do usuário do item da lista todos_obj for igual ao userid passado na url
        if todo['userId'] == userid-1:
            #adicione o item da lista todos_obj na lista user_todos
            user_todos.append(todo)
    #retorne a lista user_todos
    return user_todos

@app.route('/todos/<int:todo_id>')
def todo(todo_id):
    #retorne o item da lista todos_obj que tem o id igual ao todo_id passado na url
        return todos_obj[todo_id-1]
app.run(debug=True, port=5000)
