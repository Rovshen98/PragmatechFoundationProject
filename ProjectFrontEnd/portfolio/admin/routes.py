from flask import render_template,redirect,request,make_response
from flask.helpers import url_for
from werkzeug.utils import import_string
from modul import app,db
from modul.models import *
from modul.__init__ import *
import sqlite3



import os


ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER']= '/static/app/img'

user={
    "username":"Rovshen98",
    "password":"Melanxolik98"
}

@app.route("/login", methods=["GET","POST"])
def log():
    
    
    if request.method=="POST":
        username=request.form["username"]
        pas=request.form["pass"]

        

        if username==user["username"] and pas==user["password"]:
            resp = make_response(redirect("/admin"))
            resp.set_cookie('LoginStatus', "True")
            return resp
            
    return render_template("admin/Login_v16/index.html")

def login_required(login):
    log= request.cookies.get('LoginStatus')
    if log=="True":
        return login
    else:
        return redirect("/login")

@app.route("/logout")
def logout():
    
    resp = make_response(redirect("/login"))
    resp.set_cookie('LoginStatus', expires=0)
    return resp

@app.route("/admin")
def adminindex():
    
    return login_required(render_template ("admin/index.html"))
# fikirler++++++++++++++++++++++++++++++++++++++++++
@app.route("/admin/fikirler",methods=["GET","POST"])
def adminfikirler():
    fikirler=Fikirler.query.all()
    if request.method=="POST":
        file = request.files['fikirler-file']
        filename=file.filename
        image = os.path.join('./static/app/img/', filename)

        file.save(image)
        fikirler = Fikirler(
        file=image,
        author=request.form["fikirler-author"],
        text=request.form["fikirler-text"],
        title=request.form["fikirler-title"],
        
        )
        db.session.add(fikirler)
        db.session.commit()
        return redirect("/admin/fikirler")
    return login_required(render_template ("admin/fikirler.html", fikirler=fikirler))

@app.route("/admin/fikirler/delete/<int:id>") 
def fikirler_delete(id):
   
    fikirler= Fikirler.query.get(id)
    db.session.delete(fikirler)
    db.session.commit()
    return redirect("/admin/fikirler")

@app.route("/admin/fikirler/update/<int:id>", methods=["GET","POST"])
def fikirlerupdate(id):
    fikirler=Fikirler.query.get(id)
    if request.method=="POST":
        
        file = request.files['fikirler-file']
        filename=file.filename
        image = os.path.join('./static/app/img/', filename)

        file.save(image)
        
        fikirler.file=image
        fikirler.author=request.form["fikirler-author"]
        fikirler.text=request.form["fikirler-text"]
        fikirler.title=request.form["fikirler-title"]
        
        db.session.commit()
        

        return redirect("/admin/fikirler")
    return login_required(render_template ("admin/fikirleredit.html", fikirler=fikirler))
# /////////////////////////////////////////////////




# isler++++++++++++++++++++++++++++++++++++++++++
@app.route("/admin/isler",methods=["GET","POST"])
def adminisler():
    isler=Isler.query.all()
    if request.method=="POST":
        file = request.files['isler-file']
        filename=file.filename
        image = os.path.join('./static/app/img/', filename)

        file.save(image)
        isler = Isler(
        file=image,
        date=request.form["isler-date"],
        text=request.form["isler-text"],
        link=request.form["isler-link"],
        
        )
        db.session.add(isler)
        db.session.commit()
        return redirect("/admin/isler")
    return login_required(render_template ("admin/isler.html",isler=isler))

@app.route("/admin/isler/delete/<int:id>") 
def isler_delete(id):
   
    isler= Isler.query.get(id)
    db.session.delete(isler)
    db.session.commit()
    return redirect("/admin/isler")

@app.route("/admin/isler/update/<int:id>", methods=["GET","POST"])
def islerupdate(id):
    isler=Isler.query.get(id)
    if request.method=="POST":
        
        file = request.files['isler-file']
        filename=file.filename
        image = os.path.join('./static/app/img/', filename)

        file.save(image)
        
        isler.file=image
        isler.title=request.form["isler-title"]
        isler.text=request.form["isler-text"]
        isler.link=request.form["isler-link"]
        
        db.session.commit()
        

        return redirect("/admin/isler")
    return login_required(render_template ("admin/isleredit.html",isler=isler))

# /////////////////////////////////////////////////////

# blog+++++++++++++++++++++++++++++++++++++++++++
@app.route("/admin/blog", methods=["GET", "POST"])
def adminblog():
    
    blogs= Blog.query.all()
    if request.method=="POST":
        file = request.files['blog-file']
        filename=file.filename
        image = os.path.join('./static/app/img/', filename)

        file.save(image)
        blog = Blog(
        file=image,
        title=request.form["blog-title"],
        text=request.form["blog-text"],
        link=request.form["blog-link"],
        
        )
        db.session.add(blog)
        db.session.commit()
        return redirect("/admin/blog")
    return login_required(render_template ("admin/blog.html",blogs=blogs))

@app.route("/admin/blog/delete/<int:id>") 
def blog_delete(id):
   
    blog= Blog.query.get(id)
    db.session.delete(blog)
    db.session.commit()
    return redirect("/admin/blog")

@app.route("/admin/blog/update/<int:id>", methods=["GET","POST"])
def blogupdate(id):
    blog=Blog.query.get(id)
    if request.method=="POST":
        
        file = request.files['blog-file']
        filename=file.filename
        image = os.path.join('./static/app/img/', filename)

        file.save(image)
        
        blog.file=image
        blog.title=request.form["blog-title"]
        blog.text=request.form["blog-text"]
        blog.link=request.form["blog-link"]
        
        db.session.commit()
        

        return redirect("/admin/blog")
    return login_required(render_template ("admin/blogedit.html",blog=blog))

# /////////////////////////////////////////////////////////////

@app.route("/admin/tehsil", methods=["GET","POST"])
def admintehsiller():    
    tehsiller= Tehsil.query.all()
    if request.method=="POST":
        file = request.files['tehsil-file']
        filename=file.filename
        image = os.path.join('./static/app/img/', filename)

        file.save(image)
        tehsil =Tehsil(
        file=image,
        
        text=request.form["tehsil-text"],
        link=request.form["tehsil-link"],
        
        )
        db.session.add(tehsil)
        db.session.commit()
        return redirect("/admin/tehsil")
    return login_required(render_template ("admin/tehsil.html",tehsiller=tehsiller))

@app.route("/admin/tehsil/delete/<int:id>") 
def tehsil_delete(id):
   
    tehsil= Tehsil.query.get(id)
    db.session.delete(tehsil)
    db.session.commit()
    return redirect("/admin/tehsil")

@app.route("/admin/tehsil/update/<int:id>", methods=["GET","POST"])
def tehsilupdate(id):
    tehsil=Tehsil.query.get(id)
    if request.method=="POST":
        
        file = request.files['tehsil-file']
        filename=file.filename
        image = os.path.join('./static/app/img/', filename)

        file.save(image)
        
        tehsil.file=image
       
        tehsil.text=request.form["tehsil-text"]
        tehsil.link=request.form["tehsil-link"]
        
        db.session.commit()
        

        return redirect("/admin/tehsil")
    return login_required(render_template ("admin/tehsiledit.html",tehsil=tehsil))
    
@app.route("/admin/contact")
def contact():
    contacts=Contact.query.all()
    return login_required(render_template ("admin/contact.html",contacts=contacts))


@app.route("/admin/contact/delete/<int:id>") 
def contact_delete(id):
   
    contact= Contact.query.get(id)
    db.session.delete(contact)
    db.session.commit()
    return redirect("/admin/contact")

@app.route("/admin/contact/<int:id>")
def contactsingle(id):
    contacts=Contact.query.all()
    return login_required(render_template ("admin/contactsingle.html",contacts=contacts))


