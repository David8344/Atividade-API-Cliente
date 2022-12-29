from flask import Flask, jsonify
import json


  

  

app = Flask(__name__)
app.debug = True
#carregue o arquivo todos.json e salve na variável todos_obj
todos_obj = json.load(open('todos.json'))
#carregue o arquivo users.json e salve na variável users_obj
users_obj = json.load(open('users.json'))
#carregue o arquivo posts.json e salve na variável posts_obj
posts_obj = json.load(open('posts.json'))
#carregue o arquivo comments.json e salve na variável comments_obj
comments_obj = json.load(open('comments.json'))
#carregue o arquivo albums.json e salve na variável albums_obj
albums_obj = json.load(open('albums.json'))
#carregue o arquivo photos.json e salve na variável photos_obj
photos_obj = json.load(open('photos.json'))

#a linha abaixo que é a rota raiz
@app.route('/')
def index():
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

@app.route('/todos')
def todos():
    #retorne a variável todos_obj
    return todos_obj

@app.route('/todos/<int:todo_id>')
def todo(todo_id):
    #retorne o item da lista todos_obj que tem o id igual ao todo_id passado na url
        return todos_obj[todo_id-1]

@app.route('/posts')
def posts():
    #retorne a variável posts_obj
    return posts_obj

@app.route('/posts/<int:post_id>')
def post(post_id):
    #retorne o item da lista posts_obj que tem o id igual ao post_id passado na url
    return posts_obj[post_id-1]

@app.route('/posts/<int:post_id>/comments')
def postcomments(post_id):
    #crie uma lista vazia chamada post_comments
    post_comments = []
    #percorra todos os itens da lista comments_obj
    for comment in comments_obj:
        #se o id do post do item da lista comments_obj for igual ao post_id passado na url
        if comment['postId'] == post_id:
            #adicione o item da lista comments_obj na lista post_comments
            post_comments.append(comment)
    #retorne a lista post_comments
    return post_comments

@app.route('/comments')
def comments():
    #retorne a variável comments_obj
    return comments_obj

@app.route('/comments/<int:post_id>')
def commentspost(post_id):
    #crie uma lista vazia chamada post_comments
    comments_post = []
    #percorra todos os itens da lista comments_obj
    for comment in comments_obj:
        #se o id do post do item da lista comments_obj for igual ao post_id passado na url
        if comment['postId'] == post_id:
            #adicione o item da lista comments_obj na lista post_comments
            comments_post.append(comment)
    #retorne a lista post_comments
    return comments_post
@app.route('/comments/<int:comment_id>')
def comment(comment_id):
    #retorne o item da lista comments_obj que tem o id igual ao comment_id passado na url
    return comments_obj[comment_id-1]

@app.route('/albums')
def albums():
    #retorne a variável albums_obj
    return albums_obj
@app.route('/albums/<int:album_id>')
def album(album_id):
    #retorne o item da lista albums_obj que tem o id igual ao album_id passado na url
    return albums_obj[album_id-1]

@app.route('/albums/<int:album_id>/photos')
def albumphotos(album_id):
    #crie uma lista vazia chamada album_photos
    album_photos = []
    #percorra todos os itens da lista photos_obj
    for photo in photos_obj:
        #se o id do album do item da lista photos_obj for igual ao album_id passado na url
        if photo['albumId'] == album_id:
            #adicione o item da lista photos_obj na lista album_photos
            album_photos.append(photo)
    #retorne a lista album_photos
    return album_photos

@app.route('/photos')
def photos():
    #retorne a variável photos_obj
    return photos_obj

@app.route('/photos/<int:photo_id>')
def photo(photo_id):
    #retorne o item da lista photos_obj que tem o id igual ao photo_id passado na url
    return photos_obj[photo_id-1]

@app.route('/users/<int:user_id>/albums')
def useralbums(user_id):
    #crie uma lista vazia chamada user_albums
    user_albums = []
    #percorra todos os itens da lista albums_obj
    for album in albums_obj:
        #se o id do usuário do item da lista albums_obj for igual ao user_id passado na url
        if album['userId'] == user_id:
            #adicione o item da lista albums_obj na lista user_albums
            user_albums.append(album)
    #retorne a lista user_albums
    return user_albums


app.run(debug=True, port=5000)
