from flask import Flask
from flask import render_template, request
import requests
import MyClasses

funcoes_users = MyClasses.usuario()
funcoes_task = MyClasses.tarefas()


api_url = "http://127.0.0.1:5000/"

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/users", methods=['GET', 'POST', 'PATCH', 'DELETE'])
def users():
    if request.method == 'POST':
        title = request.form['title']
        completed = request.form['completed']
        user_id = request.form['user_id']
        todo = {
            'title': title,
            'completed': completed,
            'userId': user_id
        }
        funcoes_users.create_todo(todo)
        return 'Tarefa criada'
    else:
        users = requests.get(api_url + "users").json()
        return render_template("users.html", users=users)
@app.route("/users/<int:user_id>")
def user(user_id):
    user = requests.get(api_url + "users/"+user_id)
    
    return render_template("user.html")
@app.route("/todos")
def todos():
    todos = requests.get(api_url + "todos").json()
    return render_template("todos.html", todos=todos)

@app.route("/todos/<int:id>")
def todo(id):
    return render_template("todo.html")

app.run(debug=True, port=5001)
