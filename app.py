from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/now")
def hello_world():
    return render_template("index.html")


@app.route("/")
def CreateTemplate():
    headlinks = list()
    headlinks.append(("https://www.google.com","Google"))
    headlinks.append(("https://www.digitalocean.com","Digital Ocean"))

    navlinks = dict()
    navlinks['Compute'] = list()
    navlinks['Storage'] = list()
    navlinks['Storage'].append(("/App/anfs_vol","ANFS Volume"))
    navlinks['Compute'].append(("/App/tf_vm","Virtual Machine"))
    return render_template("gen.html", headlinks=headlinks, navlinks=navlinks)
