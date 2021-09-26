from flask import Flask,session
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin


from werkzeug.utils import secure_filename
SQLALCHEMY_TRACK_MODIFICATIONS = False


app=Flask(__name__,template_folder="../templates",static_folder="../static")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///result.db'
app.config['SECRET_KEY']="mysecret"
db=SQLAlchemy(app)



from modul.models import *
from admin.routes import *
from app.routes import *