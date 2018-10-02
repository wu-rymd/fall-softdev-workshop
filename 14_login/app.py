# Team IDoKnowYou -- Daniel Keriazis, Raymond Wu
# SoftDev pd7
# K14 -- Do I Know You?
# 2018-10-01

from flask import Flask, redirect, render_template, request, session, url_for
from util import tools

app = Flask(__name__)
app.secret_key = tools.generate_random_secretkey()

credentials = {'user':'pass'} # hardcoded user/pass combo

@app.route("/")
def homepage():
    # if already logged in
    if 'username' in session:
        return render_template("index.html", username=session['username'])
    else:
        return redirect('/login')

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":

        # if already logged in
        if 'username' in session:
            return redirect( '/' )

        # reach here: not logged in
        return render_template("login.html")

    # reach here: request.method = "POST"

    # get values passed via POST
    username = request.form.get("user")
    password = request.form.get("pass")

    # username is not a key in the dictionary of all users
    if username not in credentials.keys():
        return "Username not found! <a href='login'>Click to go back.</a>"
    # username exists, but password incorrect
    elif credentials[username] != password:
        return "Wrong password! <a href='login'>Click to go back.</a>"
    # username exists, password correct
    else:
        session['username'] = username
        return redirect('/')

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/logout")
def logout():
    session.pop('username')
    return redirect('/login')

if __name__ == "__main__":
    app.debug = False  # set to False in production mode!
    app.run()

