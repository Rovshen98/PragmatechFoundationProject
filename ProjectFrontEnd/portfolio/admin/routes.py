from flask import render_template,redirect,request
from run import app,db


@app.route("/admin")
def adminindex():
    return render_template ("admin/index.html")

@app.route("/admin/tehsil")
def admintehsil():
    return render_template("admin/tehsil.html")

@app.route("/admin/isler")
def adminisler():
    return render_template("admin/isler.html")




@app.route("/admin/blog", methods=["GET", "POST"])
def adminblog():
    from modul.models import Blog
    blogs= Blog.query.all()
    if request.method=="POST":
        
        blog = Blog(
        file=request.form["blog-file"],
        title=request.form["blog-title"],
        text=request.form["blog-text"],
        link=request.form["blog-link"],
        )
        db.session.add(blog)
        db.session.commit()
        return redirect("/admin/blog")
    return render_template("admin/blog.html",blogs=blogs)




@app.route("/admin/fikirler")
def adminfikirler():
    return render_template("admin/fikirler.html")
