from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def homepage():
    return "Hello, World!"


@app.route("/test")
def test():
    return "Hello, Test!"


@app.route("/test/hello")
@app.route("/hello")
def hello():
    return "Hey flask!"

@app.route("/user")
@app.route("/user/<name>")
def user(name = "Guest"):
    return f"Hello {name}"


@app.route("/post/<int:post_id>/comment/<int:comment_id>")
def comment(post_id, comment_id):
    return f"POST ID: {post_id}, COMMENT ID: {comment_id}"




@app.route("/welcome")
def welcome():
    ex = "This is easy"
    x = 5
    languages = ["Python", "C++", "Java", "GO", "R"]
    return render_template("index.html", extra = ex, lang = languages, x = x)



@app.route("/login", methods = ["GET", "POST"])
def login():
    error = False
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username == "admin" and password == "admin":
            error = False
            return render_template("login.html", error = error)
        else:
            error = True
            return render_template("login.html", error = error)
    return render_template("login.html")






@app.route("/api/counties")
def counties():
    counties = ["Arapahoe", "Denver", "Jefferson", "El Paso", "Boulder"]
    return jsonify({"con" : counties})




@app.route("/posts")
def posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    data = response.json()
    return jsonify(data)


@app.route("/posts/<int:post_id>")
def post(post_id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}")
    data = response.json()['title']
    return jsonify(data)






if __name__ == "__main__":
    app.run(debug=True )