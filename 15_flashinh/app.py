# Team IDoKnowYou -- Daniel Keriazis, Raymond Wu
# SoftDev pd7
# K15 -- Oh yes, perhaps I do…
# 2018-10-02

from flask import Flask, redirect, render_template, request, session, url_for, flash
import util.tools as tools

app = Flask(__name__)
app.secret_key = tools.generate_random_secretkey()

credentials = {'user':'pass'} # Hardcoded user/pass combo

@app.route("/")
def homepage():
    if 'username' in session:  # Already logged in
        return render_template("index.html", username=session['username'])
    else:
        return redirect('/login')

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        if 'username' in session:  # Already logged in
            return redirect( '/' )
        else:
            return render_template("login.html")

    # Get values passed via POST
    username = request.form.get("user")
    password = request.form.get("pass")

    if username not in credentials:  # Username doesn't exist
        flash('Username not found!')
    elif credentials[username] != password:  # Username exists, incorrect password
        flash('Wrong password!')
    else:  # Username exists, password correct
        session['username'] = username
        return redirect('/')
    return render_template('login.html')

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/logout")
def logout():
    session.pop('username')
    return redirect('/login')

if __name__ == "__main__":
    app.debug = False  # set to False in production mode
    app.run()

