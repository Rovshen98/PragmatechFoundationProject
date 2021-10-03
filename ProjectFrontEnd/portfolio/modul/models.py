
from modul import db


class Blog(db.Model):
    __tablename__ = 'blog'
    id= db.Column(db.Integer, primary_key=True)
    title= db.Column(db.String(80))
    text= db.Column(db.String(120))
    link=db.Column(db.String(400))
    file= db.Column(db.String(100))

    def __init__(self,title,text,link,file):
        self.title = title
        self.text = text
        self.link = link
        self.file = file


class Isler(db.Model):
    __tablename__ = 'isler'
    id= db.Column(db.Integer, primary_key=True)
    date= db.Column(db.String(80))
    text= db.Column(db.String(120))
    link=db.Column(db.String(400))
    file= db.Column(db.String(100))

    def __init__(self,date,text,link,file):
        self.date = date
        self.text = text
        self.link = link
        self.file = file


class Fikirler(db.Model):
    __tablename__ = 'fikirler'
    id= db.Column(db.Integer, primary_key=True)
    author= db.Column(db.String(80))
    text= db.Column(db.String(120))
    title=db.Column(db.String(400))
    file= db.Column(db.String(100))

    def __init__(self,author,text,title,file):
        self.author = author
        self.text = text
        self.title = title
        self.file = file

class Tehsil(db.Model):
    __tablename__ = 'tehsil'
    id= db.Column(db.Integer, primary_key=True)
    link= db.Column(db.String(400))
    text=db.Column(db.String(400))
    file= db.Column(db.String(100))

    def __init__(self,link,text,file):
        self.link = link
        self.text = text
        self.file = file

class Contact(db.Model):
    __tablename__ = 'contact'
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(100))
    email=db.Column(db.String(100))
    subject= db.Column(db.String(400))
    message=db.Column(db.String(1000))

    def __init__(self,name,email,subject,message):
        self.name = name
        self.email = email
        self.subject = subject
        self.message = message

class User(db.Model):
    __tablename__ = 'user'
    id= db.Column(db.Integer, primary_key=True)
    username= db.Column(db.String(100))
    password=db.Column(db.String(100))
    

    def __init__(self,username,password):
        self.username = username
        self.password = password
        





