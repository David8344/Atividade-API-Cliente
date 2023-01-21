from flask import request
import requests

api_url = "localhost:5000/"

class delete:
    def __init__(self, id):
        self.id = id

    def delete_user(self):
        id_user = request.form.get("id_todo_action")
        url = api_url + "users/{}".format(id_user)
        response = requests.delete(url)
        if response.status_code == 200:
            return response.status_code
        else:
            print('Erro ao apagar usuario!')
        return response.status_code

    def delete_todo(self):
        id_todo = request.form.get("id_todo_action")
        url = api_url + "todos/{}".format(id_todo)
        response = requests.delete(url)
        if response.status_code == 200:
            return response.status_code
        else:
            print('Erro ao apagar tarefa!')
        return response.status_code

class update :
    def __init__(self, id):
        self.id = id

    def update_user(self):
        id_user = request.form.get("id_todo_action")
        url = api_url + "users/{}".format(id_user)
        response = requests.put(url)
        if response.status_code == 200:
            return response.status_code
        else:
            print('Erro ao atualizar usuario!')
        return response.status_code

    def update_todo(self):
        id_todo = request.form.get("id_todo_action")
        url = api_url + "todos/{}".format(id_todo)
        response = requests.put(url)
        if response.status_code == 200:
            return response.status_code
        else:
            print('Erro ao atualizar tarefa!')
        return response.status_code
        