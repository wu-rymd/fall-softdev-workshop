from urllib import request #stdlib
import json #stdlib

from flask import Flask, render_template #pip install flask

app = Flask(__name__)

# ========== The New York Times Top Stories API ==========

NYT_KEY  = "49fa4b3075954f5091ec2bf5a508954f"
NYT_STUB = "https://api.nytimes.com/svc/topstories/v2/home.json?api-key="
NYT_URL  = NYT_STUB + NYT_KEY

u = request.urlopen(NYT_URL)
response = u.read()
data = json.loads(response)

# Display top story headline w/ link
NYT_TOPSTORY = data['results'][0]['title']
NYT_LINK = data['results'][0]['url']

# ========== Dark Sky API ==========

DSKY_KEY   = "7b7da681bded1d4c80f763a683ca56ac"
DSKY_STUB  = "https://api.darksky.net/forecast/"
DSKY_COORD = "40.718157,-74.013784"
DSKY_URL   = DSKY_STUB + DSKY_KEY + "/" + DSKY_COORD

u = request.urlopen(DSKY_URL)
response = u.read()
data = json.loads(response)

# Display weather condition and degrees
DSKY_WEATHER = data['currently']['summary']
DSKY_DEGREES = data['currently']['temperature']

# ========== ISS Current Location API ==========

ISS_URL = "http://api.open-notify.org/iss-now.json"

u = request.urlopen(ISS_URL)
response = u.read()
data = json.loads(response)

# Display tiemstamp and coordinates of ISS
ISS_TIME = data['timestamp']
ISS_LAT  = data['iss_position']['latitude']
ISS_LONG = data['iss_position']['longitude']

@app.route("/")
def root():
    return render_template("base.html",
                           link = NYT_LINK,
                           top_story = NYT_TOPSTORY,
                           weather = DSKY_WEATHER,
                           degrees = DSKY_DEGREES,
                           time = ISS_TIME,
                           latitude = ISS_LAT,
                           longitude = ISS_LONG)

if __name__ == "__main__":
    app.debug = True  # set to False in production mode!
    app.run()
