import datetime

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    now = datetime.datetime.now()
    new_year = now.month==1 and now.day==1
    return render_template("hello.html", new_year = new_year)

@app.route("/<string:name>")
def Peter(name):
    return f"<h1>Hello,{name}</h1>"

@app.route("/more")
def more():
    return render_template("more.html")
