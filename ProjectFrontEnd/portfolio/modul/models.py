
from modul import db


class Blog(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    title= db.Column(db.String(80))
    text= db.Column(db.String(120))
    link=db.Column(db.String(400))
    file= db.Column(db.String(100));

class Isler(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    date= db.Column(db.String(80))
    text= db.Column(db.String(120))
    link=db.Column(db.String(400))
    file= db.Column(db.String(100));

class Fikirler(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    author= db.Column(db.String(80))
    text= db.Column(db.String(120))
    title=db.Column(db.String(400))
    file= db.Column(db.String(100));

class Tehsil(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    link= db.Column(db.String(400))
    text=db.Column(db.String(400))
    file= db.Column(db.String(100));

class Contact(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(100))
    email=db.Column(db.String(100))
    subject= db.Column(db.String(400))
    message=db.Column(db.String(1000));




