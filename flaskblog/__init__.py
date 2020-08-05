from flask import Flask #render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__) #import to __init__ file
app.config['SECRET_KEY'] = '7dbf59ce34f44313006c239fdd74c73c'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' 

db = SQLAlchemy(app) #DB instance

from flaskblog import routes