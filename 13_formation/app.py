# Raymond Wu
# SoftDev pd7
# K10 -- Echo Echo Echo
# 2018-09-28

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def homepage():
    print (app)
    return "<a href='form'>Go to /form</a>"

@app.route("/form")
def htmlForm():
    return render_template("form.html")

@app.route("/auth")
def authenticate():
    # print(app)
    # print(request)
    # print(request.args)
    # print(request.args['username'])
    # print(request.headers)
    return render_template( "auth.html",
                                username = request.args['username'],
                                requestMethod = request.method )


if __name__ == "__main__":
    app.debug = True  # set to False in production mode
    app.run()
