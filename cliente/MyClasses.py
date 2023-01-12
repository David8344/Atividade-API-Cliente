
from urllib import response
import requests
api_users = "https://jsonplaceholder.typicode.com/users/"
api_tasks = "https://jsonplaceholder.typicode.com/todos/"

class usuario:

    def ler():
        response = requests.get(api_users)
        usuarios = response.json()
        for usuario in usuarios:
            print(usuario["id"], usuario["name"])
            
    def criar():
        nome = input("digite o nome do usuario")
        username = input("digite o nome de usuario")
        email = input("digite o email do usuario")
        response = requests.post(api_users, data = {"name": nome, "username": username, "email": email})
        if response.status_code == 201:
            print("usuario criado")
        else:
            print("não foi possivel criar o usuario")

    def atualizar():
        id = input("Digite o id do usuário: ")
        response = requests.get(api_users + id)
        if response.status_code == 200:
            user =response.json()
            print("Usuario com o nome: [", user["name"], "] encontrado")
            print("Digite os novos dados do usuário")
            nome = input("Digite o nome do usuário: ")
            username = input("Digite o username de usuário: ")
            email = input("Digite o email do usuário: ")
            response = requests.put(api_users + id, data = {"name": nome, "username": username, "email": email})
            print()
            print(response.status_code)
            print()

    def deletar():
        id = input("Digite o id do usuário: ")
        response = requests.get(api_users + id)
        if response.status_code == 200:
            user =response.json()
            print("Usuario com o nome: [", user["name"], "] encontrado")
            print()
            print("Deseja realmente deletar o usuário?")
            opcao = input("Digite 1 para sim e 2 para não: ")
            if opcao == "1":
                response = requests.delete(api_users + id)
                print()
                print(response.status_code)
                print()
            elif opcao == "2":
                print("Usuário não deletado")
                print()
            else:
                print("Opção inválida")
                print()
        else:
            print("Usuário não encontrado")
            print()


class tarefas:

    def ler():
        id = input("Digite o id do usuário: ")
        response = requests.get(api_users + id +"/todos" )
        if response.status_code == 200:
            tasks = response.json()
            for task in tasks:
                print("Titulo: ", task["title"])
                print("Status: ", task["completed"])
    
    def criar():
        id = input("digite a id do usuario que a tarefa pertence ")
        titulo = input("digite o titulo da tarefa ")
        status = input("digite se a tarefa esta completa ou não (True|False) ")
        response = requests.post(api_users + id +"/todos", data = {"userId": id, "title": titulo, "status": status})
        if response.status_code == 201:
            print("tarefa criada")
    
    def atualizar():
        id = input("Digite o id da tarefa: ")
        response = requests.get(api_tasks + id)
        if response.status_code == 200:
            task =response.json()
            print("Tarefa com o título: [", task["title"], "] encontrada")
            print("Status: ", task["completed"])
            print()
            print()
            print("Digite os dados da tarefa")
            titulo = input("Digite o título da tarefa: ")
            status = input("Digite o status da tarefa: ")
            user = input("digite o id do usuario que ira realizar a tarefa ")
            response = requests.put(api_tasks + id, data = {"userId": user, "title": titulo, "completed": status})
            print()
            print(response.status_code)
            print()

    def deletar():
        print()
        id_tasks = input("Digite o id da tarefa: ")
        response = requests.get(api_tasks + id_tasks)
        if response.status_code == 200:
            task =response.json()
            print("Tarefa com o título: [", task["title"], "] encontrada")
            print("Status: ", task["completed"])
            print()
            print("Deseja realmente deletar a tarefa?")
            opcao = input("Digite 1 para sim e 2 para não: ")
            if opcao == "1":
                response = requests.delete(api_tasks + id_tasks)
                print()
                print(response.status_code)
                print()
            elif opcao == "2":
                print("Tarefa não deletada")
                print()
            else:
                print("Opção inválida")
                print()
        else:
            print("Tarefa não encontrada")
            print()
        return 0
