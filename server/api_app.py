from flask import Flask, jsonify, request, Response
import json, requests


app = Flask(__name__)
app.debug = True

todos_obj = json.load(open('todos.json'))
users_obj = json.load(open('users.json'))
posts_obj = json.load(open('posts.json'))
comments_obj = json.load(open('comments.json'))
albums_obj = json.load(open('albums.json'))
photos_obj = json.load(open('photos.json'))

@app.route('/')
def index():
    return todos_obj

@app.route('/users', methods=['GET',])
def get_users():
        return users_obj

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    users_obj.append(data)
    return jsonify(data)

@app.route('/users/<int:user_id>', methods=['PATCH'])
def update_user(user_id):
    data = request.get_json()
    users_obj[user_id-1] = data
    return jsonify(data)

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    users_obj.pop(user_id-1)
    return jsonify({'success': True})
   


@app.route('/users/<int:user_id>')
def user(user_id):
    return users_obj[user_id-1]

@app.route("/users/<int:userid>/todos")
def usertodos(userid):
    user_todos = []
    for todo in todos_obj:
        if todo['userId'] == userid-1:
            user_todos.append(todo)
    return user_todos

@app.route('/todos', methods=['GET'])
def get_todos():
        return todos_obj

@app.route('/todos/new', methods=['POST'])
def create_todo():
    data = request.get_json()
    todos_obj.append(data)
    return jsonify(data)

@app.route('/todos/<int:todo_id>/update', methods=['PATCH'])
def update_todo(todo_id):
    data = request.get_json()
    todos_obj[todo_id-1] = data
    return jsonify(data)

@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    todos_obj.pop(todo_id-1)
    return jsonify({'success': True})


@app.route('/todos/<int:todo_id>')
def todo(todo_id):
        return todos_obj[todo_id-1]

@app.route('/posts')
def posts():
    return posts_obj

@app.route('/posts/<int:post_id>')
def post(post_id):
    return posts_obj[post_id-1]

@app.route('/posts/<int:post_id>/comments')
def postcomments(post_id):
    post_comments = []
    for comment in comments_obj:
        if comment['postId'] == post_id:
            post_comments.append(comment)
    return post_comments

@app.route('/comments')
def comments():
    return comments_obj

@app.route('/comments/<int:post_id>')
def commentspost(post_id):
    comments_post = []
    for comment in comments_obj:
        if comment['postId'] == post_id:
            comments_post.append(comment)
    return comments_post
@app.route('/comments/<int:comment_id>')
def comment(comment_id):
    return comments_obj[comment_id-1]

@app.route('/albums')
def albums():
    return albums_obj
@app.route('/albums/<int:album_id>')
def album(album_id):
    return albums_obj[album_id-1]

@app.route('/albums/<int:album_id>/photos')
def albumphotos(album_id):
    album_photos = []
    for photo in photos_obj:
        if photo['albumId'] == album_id:
            album_photos.append(photo)
    return album_photos

@app.route('/photos')
def photos():
    return photos_obj

@app.route('/photos/<int:photo_id>')
def photo(photo_id):
    return photos_obj[photo_id-1]

@app.route('/users/<int:user_id>/albums')
def useralbums(user_id):
    user_albums = []
    for album in albums_obj:
        if album['userId'] == user_id:
            user_albums.append(album)
    return user_albums


app.run(debug=True, port=5000)
