from flask_sqlalchemy import SQLAlchemy

from run import db,app
db=SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///result.db'
class Blog(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    title= db.Column(db.String(80))
    text= db.Column(db.String(120))
    link=db.Column(db.String(400))
    file= db.Column(db.String(100))