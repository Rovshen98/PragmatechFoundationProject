from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage

import os



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ted.db'
db = SQLAlchemy(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SERCER_KEY'] = 't53424u6756432456u56546342'
app.config['UPLOAD_FOLDER']= 'oxu.az/static/uploads'

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.String(80))
    month = db.Column(db.String(120))
    time = db.Column(db.String(120))
    title = db.Column(db.String(120))
    content = db.Column(db.String(120))
    file=db.Column(db.String(100))

@app.route("/", methods=["GET","POST"])
def createnews():
    
    if request.method=="POST":
        file = request.files['file']
        filename=secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
      
        day=request.form["day"]
        month=request.form["month"]
        time=request.form["time"]
        title=request.form["title"]
        content=request.form["content"]
        
        
        data = User(
            day=day,
            month=month,
            time=time,
            title=title,
            content=content,
            file=file
        )
        db.session.add(data)
        db.session.commit()
        return redirect("/index")
    return render_template("admin.html")

@app.route("/index")
def index():
    News=User.query.all()
    return render_template("index.html",blog=News)
    




if __name__=="__main__":
    app.run(debug=True)