from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import psycopg2



from werkzeug.utils import secure_filename
app=Flask(__name__,template_folder="../templates",static_folder="../static")


ENV="dev"
if ENV=="dev":
    app.debug=True  
    app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://postgres:duligidagadi@localhost:5433/consult'
else:
   app.debug=True
   app.config['DATABASE_URL'] = 'postgres://njsjkdwpyuoriy:879d60f7955321eb1bee7127e8915e95002eced7b73602e1017d711eda1b7524@ec2-54-204-148-110.compute-1.amazonaws.com:5432/d1mur9nd867b7o'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

app.config['SECRET_KEY']="secretgarden"
db=SQLAlchemy(app)



from modul.models import *
from admin.routes import *
from app.routes import *
