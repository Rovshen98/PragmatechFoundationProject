from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)
db=SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///result.db'

from app.routes import *
from admin.routes import *

if __name__=='__main__':
    app.run(debug = True)