from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ted.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.String(80))
    month = db.Column(db.String(120))
    time = db.Column(db.String(120))
    title = db.Column(db.String(120))
    content = db.Column(db.String(120))

@app.route("/", methods=["GET","POST"])
def createnews():
    News=User.query.all()
    if request.method=="POST":
       
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
            content=content
        )
        db.session.add(User)
        db.session.commit()
        return redirect("/index")
    return render_template("admin.html")

@app.route("/index")
def index():
    
    return render_template("admin.html")
    




if __name__=="__main__":
    app.run(debug=True)