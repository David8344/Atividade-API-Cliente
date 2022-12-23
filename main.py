from flask import Flask
from flask import render_template, request
import requests


api_url = "https://jsonplaceholder.typicode.com/"

app = Flask(__name__)

@app.route("/")
def index():
    template = "index.html"
    return render_template(template)

@app.route("/users", methods=['GET', 'POST'])
def users():
    template = "users.html"
    users = requests.get(api_url + "users").json()

    if request.method == 'POST':
        id_user_delete = request.form.get('id_user_delete')
        url_delete = api_url + "users/" + id_user_delete
        if requests.get(url_delete).status_code == 200:
            requests.delete(url_delete)
            users = requests.get(api_url + "users").json()
            return render_template(template, users=users, message="Usuário apagado com sucesso!", class_alert="alert-success")
        else:
            print("User not found")
            return render_template(template, users=users, message="Erro ao apagar usuário, talvez o usuário não exista! ", class_alert="alert-danger")

    return render_template(template, users=users)

#criar um novo usuário do jsonplacehoder
@app.route("/users/new", methods=['GET', 'POST'])
def new_user():
    template = "new_user.html"
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        username = request.form.get('username')
        phone = request.form.get('phone')
        website = request.form.get('website')
        company_name = request.form.get('company_name')
        eddress_street = request.form.get('eddress_street')
        eddress_suite = request.form.get('eddress_suite')
        eddress_city = request.form.get('eddress_city')
        eddress_zipcode = request.form.get('eddress_zipcode')
        eddress_geo_lat = request.form.get('eddress_geo_lat')
        eddress_geo_lng = request.form.get('eddress_geo_lng')

        data = {
            "name": name,
            "email": email,
            "username": username,
            "phone": phone,
            "website": website,
            "company": {
                "name": company_name
            },
            "address": {
                "street": eddress_street,
                "suite": eddress_suite,
                "city": eddress_city,
                "zipcode": eddress_zipcode,
                "geo": {
                    "lat": eddress_geo_lat,
                    "lng": eddress_geo_lng
                }
            }
        }
        requests.post(api_url + "users", data=data)
        return render_template(template, message="Usuário criado com sucesso!", class_alert="alert-success")
    return render_template(template)


@app.route("/users/<int:user_id>")
def user_details(user_id):
    template = "user_details.html"
    # Get user details
    user = requests.get(api_url + "users/{}".format(user_id)).json()
    # Get user posts
    posts = requests.get(api_url + "posts?userId={}".format(user_id)).json()
    # Get user albums
    albums = requests.get(api_url + "albums?userId={}".format(user_id)).json()
    #Get user todos
    todos = requests.get(api_url + "todos?userId={}".format(user_id)).json()
    return render_template(template, user=user, posts=posts, albums=albums, todos=todos)
 

if __name__ == "__main__":
    app.secret_key = "jsonplaceholder"
    app.run(debug=True)
