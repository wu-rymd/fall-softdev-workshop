from flask import Flask, render_template, session
from util import tools

app = Flask(__name__)

app.secret_key = tools.generate_random_secretkey()

@app.route("/", methods=["GET", "POST"])
def homepage():
    return render_template("index.html", username=username)

@app.route("/auth", methods=["POST"])
def auth():
    return ""

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

if __name__ == "__main__":
    app.debug = True  # set to False in production mode!
    app.run()

