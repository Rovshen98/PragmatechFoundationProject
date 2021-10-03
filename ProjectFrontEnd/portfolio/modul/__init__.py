from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import psycopg2



from werkzeug.utils import secure_filename
app=Flask(__name__,template_folder="../templates",static_folder="../static")


ENV="prod"
if ENV=="dev":
    app.debug=True  
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:duligidagadi@localhost/lexus'
else:
   app.debug=False
   app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://jqxscfjjdemkui:637117ed3300f66b596ccfef6da9273177a8dc12a31c8d328b93363dd55f24b1@ec2-3-218-47-9.compute-1.amazonaws.com:5432/d81q09r9plfrbp'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

app.config['SECRET_KEY']="mysecret"
db=SQLAlchemy(app)

db.create_all()

from modul.models import *
from admin.routes import *
from app.routes import *
