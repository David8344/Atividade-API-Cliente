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

@app.route("/users" , methods=['GET'])
def users():
    users = requests.get(api_url + "users").json()
    return render_template("users.html", users=users)

@app.route("/todos", methods=['GET',])
def todos():
    todos = requests.get(api_url + "todos").json()
    return render_template("todos.html", todos=todos)

@app.route("/users/new", methods=['GET','POST'])
def create_users():
    users = requests.get(api_url + "users").json()
    if request.method == 'POST':
        name = request.form['name']
        username = request.form['username']
        email = request.form['email']
        phone = request.form['phone']
        website = request.form['website']
        company = request.form['company']
        address_suite = request.form['address_suite']
        city = request.form['city']
        address_street = request.form['address_street']
        zipcode = request.form['zipcode']
        lat = request.form['lat']
        lng = request.form['lng']
        user = {"address":{
                'city': city,
                'geo': { 'lat': lat, 'lng': lng },
                'street': address_street,
                'suite': address_suite,
                'zipcode': zipcode
            },
            'name': name,
            'username': username,
            'email': email,
            'phone': phone,
            'website': website,
            'company': company,
            'zipcode': zipcode,
       
        }
        if requests.get(api_url + "users").status_code == 200:
            return render_template('new_user.html', message="Usuário criado com sucesso!", class_alert="alert-success")
        else:
            return render_template('new_user.html', message="Erro ao apagar usuário, talvez o usuário não exista! ", class_alert="alert-danger")
    else:
        return render_template("new_user.html")

@app.route("/todos/new", methods=['GET', 'POST'])
def create_todo():
    todos = requests.get(api_url + "todos").json()
    if request.method == 'POST':
        title = request.form['title']
        completed = request.form['completed']
        user_id = request.form['user_id']
        todo = {
            'title': title,
            'completed': completed,
            'user_id': user_id
        }
        if requests.get(api_url + "todos").status_code == 200:
            return render_template('new_todo.html', message="Tarefa criada com sucesso!", class_alert="alert-success")
        else:
            return render_template('new_todo.html', message="Erro ao criar tarefa, talvez o usuário não exista! ", class_alert="alert-danger")
    else:
        return render_template("new_todo.html")
@app.route("/users/<int:user_id>")
def user(user_id):
    user = requests.get(api_url + "users/{}".format(user_id)).json()
    return render_template("user.html", user=user)

@app.route("/todos/<int:todo_id>")
def todo(todo_id):
    todo = requests.get(api_url + "todos/{}".format(todo_id)).json()
    return render_template("todo.html", todo=todo)

@app.route("/users/<int:userid>/todos")
def usertodos(user_id):
    user_todos = requests.get(api_url + "users/{}todos".format(user_id)).json()
    return render_template('user_todos.html', user_todos=user_todos)


  
@app.route("/users/update/<int:user_id>", methods=['GET','PATCH', 'POST'])
def update_users(user_id):
    if request.method == 'POST':
        name = request.form['name']
        username = request.form['username']
        email = request.form['email']
        user = {
            'name': name,
            'username': username,
            'email': email
        }
        if requests.get(api_url + "users").status_code == 200:
            return render_template('update_user.html', message="Usuario atualizado com sucesso!", class_alert="alert-success")
        else:
            return render_template('update_user.html', message="Erro ao atualizar usuario! ", class_alert="alert-danger")

    else:
        return render_template("update_user.html")

@app.route("/todos/update/<int:todo_id>", methods=['GET','PATCH', 'POST'])
def update_todos(todo_id):
    if request.method == 'POST':
        title = request.form['title']
        completed = request.form['completed']
        todo = {
            'title': title,
            'completed': completed
        }
        if requests.get(api_url + "todos").status_code == 200:
            return render_template('update_todo.html', message="Tarefa atualizada com sucesso!", class_alert="alert-success")
        else:
            return render_template('update_todo.html', message="Erro ao atualizar tarefa! ", class_alert="alert-danger")
    else:
        return render_template("update_todo.html")
       

@app.route("/users/delete/<int:user_id>", methods=['DELETE', 'GET', 'POST'])
def delete_user(user_id):
    if request.method == 'POST':
        if requests.get(api_url + "users").status_code == 200:
            return render_template('users.html', message="Usuario deletado com sucesso!", class_alert="alert-success")
        else:
            return render_template('users.html', message="Erro ao apagar usuario, talvez o usuario não exista! ", class_alert="alert-danger")
    else:
        user = requests.get(api_url + "users/{}".format(user_id)).json()
        return render_template("delete_user.html", user=user)

@app.route("/todos/delete/<int:todo_id>", methods=['DELETE', 'GET', 'POST'])
def delete_todo(todo_id):
    todo = requests.get(api_url + "todos/{}".format(todo_id)).json()
    if request.method == 'POST':
        if requests.get(api_url + "todos").status_code == 200:
            return render_template('todos.html', message="Tarefa deletada com sucesso!", class_alert="alert-success")
        else:
            return render_template('todos.html', message="Erro ao apagar tarefa, talvez a tarefa não exista! ", class_alert="alert-danger")
    else:
        return render_template("delete_todo.html", todo=todo)


app.run(debug=True, port=5001)
