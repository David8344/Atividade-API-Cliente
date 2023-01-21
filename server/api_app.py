from flask import Flask, jsonify, request, Response, make_response
import json, requests


app = Flask(__name__)
app.debug = True

users_obj = json.load(open('users.json'))
todos_obj = json.load(open('todos.json'))


@app.route('/')
def index():
    return todos_obj

@app.route('/users', methods=['GET',])
def get_users():
    make_response(
        jsonify(users_obj), 200
        )
    return users_obj
@app.route('/todos', methods=['GET'])
def get_todos():
    make_response(
        jsonify(todos_obj), 200
        )
    return todos_obj

@app.route('/users/new', methods=['POST'])
def create_user():
    data = request.get_json()
    data['id'] = len(users_obj) + 1
    with open('users.json', 'a') as f:
        json.dump(data, f)
    return jsonify(data)

@app.route('/todos/new', methods=['POST'])
def create_todo():
    data = request.get_json()
    data['id'] = len(todos_obj) + 1
    with open('todos.json', 'a') as f:
        json.dump(data, f)
    return jsonify(data)

@app.route('/users/<int:user_id>', methods=['PATCH'])
def update_user(user_id):
    data = request.get_json()
    data['id'] = len(users_obj) + 1

    users_obj[user_id-1] = data
    return make_response(jsonify(data), 201)

@app.route('/todos/<int:todo_id>/update', methods=['PATCH'])
def update_todo(todo_id):
    data = request.get_json()
    todos_obj[todo_id-1] = data
    return jsonify(data)

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    users_obj.pop(user_id-1)
    return make_response ({'success': True})

@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    todos_obj.pop(todo_id-1)
    return jsonify({'success': True})


@app.route('/users/<int:user_id>')
def user(user_id):
    return users_obj[user_id-1]

@app.route('/todos/<int:todo_id>')
def todo(todo_id):
        return todos_obj[todo_id-1]

@app.route("/users/<int:userid>/todos")
def usertodos(userid):
    user_todos = []
    for todo in todos_obj:
        if todo['userId'] == userid-1:
            user_todos.append(todo)
    return user_todos





app.run(debug=True, port=5000)
