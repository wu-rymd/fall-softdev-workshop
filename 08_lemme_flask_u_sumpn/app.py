# Raymond Wu
# SoftDev1 pd7
# K08 -- Fill Yer Flask
# 2018-09-20

from flask import Flask
app = Flask(__name__)

@app.route("/")
def helloWorld():
    return ("Hello, world!")

@app.route("/<name>")
def lab251BestLab(name):
    return ("Hello, my name is {}! My favorite text editor is <b>Emacs</b>.").format(name)

@app.route("/kts")
def keysToSuccess():
    html="""
    <p><b>Success</b> can be defined as</p> 
    <ul>
    <li><b>the accomplishment of an aim or purpose</b> (Google),</li> 
    <li><b>achievement of a goal, for example academic achievement</b> (Wikipedia), or</li>
    <li><b>sticking with what matters through hard times</b> (TED).</li>
    </ul>
    <p>Therefore, it is necessary to <b>struggle</b> each time you aim to accomplish your nightly goals.</p>
    <p>Here are some ways to faciliate learnination:</p>
    <ul>
    <li><b>csDojo!</b> Open every R 15:35-16:55!</li>
    <li><b>KEYS TO SUCCESS!</b> <small>aptly named, of course...</small></li>
    <li><b>QAF!</b> great place to provide & get help...</li>
    <li><b>Keep notes</b> of specific nuances, questions... <em>ask why?</em></li> 
    </ul>
    <p>&mdash;raywu of the past, present, and future</p>
"""
    return (html)

if __name__ == "__main__":
    app.debug = True
    app.run()
