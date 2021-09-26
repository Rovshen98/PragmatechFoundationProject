from flask import render_template,redirect,request,url_for
from werkzeug.utils import import_string
from modul import app
from modul.models import *


@app.route("/esassehife")
def blueprint():
    
    return render_template ("app/index.html")

@app.route("/app/blog", methods=["GET","POST"])
def appblog():
    
    blogs= Blog.query.all()
    return render_template("app/blog.html",blogs=blogs)

@app.route("/app/isler", methods=["GET","POST"])
def appisler():
    
    isler= Isler.query.all()
    return render_template("app/isler.html",isler=isler)

@app.route("/app/fikirler", methods=["GET","POST"])
def appfikirler():
    
    fikirler=Fikirler.query.all()
    return render_template("app/fikirler.html",fikirler=fikirler)

@app.route("/app/tehsil", methods=["GET","POST"])
def apptehsil():
    
    tehsiller=Tehsil.query.all()
    return render_template("app/tehsil.html",tehsiller=tehsiller)


@app.route("/app/elaqe", methods=["GET","POST"])
def appcontact():
    
    if request.method=="POST":
        contact=Contact(
        name= request.form["name"],
        email=request.form["email"],
        subject=request.form["subject"],
        message=request.form["message"])
        db.session.add(contact)
        db.session.commit()
        
    return render_template ("app/elaqe.html")