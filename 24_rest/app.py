# Mai Rachlevsky, Raymond Wu (team BlueBalloons)
# SoftDev1 pd7
# K24 -- A RESTful Journey Skyward
# 2018-11-14

from flask import Flask, render_template
import urllib
import json

app = Flask(__name__)

# do this once and once only!
u = urllib.urlopen("https://api.nasa.gov/planetary/earth/imagery/?lon=100.75&lat=1.5&date=2014-02-01&cloud_score=True&api_key=F6TDwiEwmUJItcVH4X9NYeooLACkUVDnXsyeqGhL")
response = u.read()
data = json.loads(response)
imgSrc = data['url']

@app.route("/")
def homepage():
    return render_template("base.html",
                               pic=imgSrc)

if __name__ == "__main__":
    app.debug = True  # set to False in production mode!
    app.run()
