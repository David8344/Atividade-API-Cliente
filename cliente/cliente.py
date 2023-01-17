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

@app.route("/users/new", methods=['GET','POST'])
def create_users():
    
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
        user = {
            'name': name,
            'username': username,
            'email': email,
            'phone': phone,
            'website': website,
            'company': company,
            'eddress_suite': address_suite,
            'city': city,
            'address_street': address_street,
            'zipcode': zipcode,
            'lat': lat,
            'lng': lng
        }
        funcoes_users.create_user(user)
        return 'Usuário criado'
    else:
        return render_template("new_user.html")
  
@app.route("/users/<int:user_id>/update", methods=['GET','PATCH'])
def update_users(user_id):
    if request.method == 'PATCH':
        name = request.form['name']
        username = request.form['username']
        email = request.form['email']
        user = {
            'name': name,
            'username': username,
            'email': email
        }
        funcoes_users.update_user(user)

        return 'Usuário atualizado'
    else:
        return render_template("update_user.html")
       

@app.route("/users/<int:user_id>/delete", methods=['DELETE'])
def delete_user(user_id):
    funcoes_users.delete_user(user_id)
    return 'Usuário deletado'

@app.route("/users/<int:user_id>")
def user(user_id):
    user = requests.get(api_url + "users/{}".format(user_id)).json()
    return render_template("user.html", user=user)
    
@app.route("/todos")
def todos():
    todos = requests.get(api_url + "todos").json()
    return render_template("todos.html", todos=todos)



@app.route("/todos/new", methods=['GET', 'POST'])
def new_todo():
    return render_template("new_todo.html")

@app.route("/todos/<int:id>")
def todo(id):
    return render_template("todo.html")



app.run(debug=True, port=5001)
