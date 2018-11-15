# Raymond Wu
# SoftDev1 pd7
# K25 -- Getting More REST
# 2018-11-15

import urllib         #stdlib
import json           #stdlib

from flask import Flask, render_template #pip install flask

app = Flask(__name__)

NASA_KEY = "F6TDwiEwmUJItcVH4X9NYeooLACkUVDnXsyeqGhL"
URL_STUB = "https://api.nasa.gov/planetary/earth/imagery/?lon=100.75&lat=1.5&date=2014-02-01&cloud_score=True&api_key="
URL = URL_STUB + NASA_KEY

# do this once and once only!
u = urllib.request.urlopen(URL)
response = u.read()
data = json.loads(response)
imgSrc = data['url']

USDA_KEY = "ldLj8pq7XcUKiLQP3AvUsUh6v3It05DuDKk7zaN1"
URL_STUB = "https://api.nal.usda.gov/ndb/search/?q=cheese&format=json&max=5&api_key="
URL = URL_STUB + USDA_KEY

u = urllib.request.urlopen(URL)
response = u.read()
data = json.loads(response)
foodName = data['list']['item'][0]['name']

@app.route("/")
def homepage():
    return render_template("base.html",
                           pic=imgSrc,
                           food=foodName)

if __name__ == "__main__":
    app.debug = True  # set to False in production mode!
    app.run()
