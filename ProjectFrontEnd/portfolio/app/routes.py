from flask import render_template,redirect,request
from run import app

@app.route("/")
def appindex():
    return render_template ("app/index.html")

