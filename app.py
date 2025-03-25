from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/tempate-creator")
def CreateTemplate():
    links = list()
    links.append(("www.google.com","Google"))
    links.append(("www.digitalocean.com","Digital Ocean"))
    
    return render_template("gen.html", links=links)
