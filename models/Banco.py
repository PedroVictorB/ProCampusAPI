from flask.ext.heroku import Heroku

__author__ = 'pedro'

import datetime
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import DateTime, Column
from flask import Flask

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost/procampus'
heroku = Heroku(app)
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(40))
    email = db.Column(db.String(80), unique=True)
    date = Column(DateTime, default=datetime.datetime.utcnow)


class Problem(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(40))
    category = db.Column(db.String(40))
    description = db.Column(db.String(40))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    date = Column(DateTime, default=datetime.datetime.utcnow)
    user = db.Column(db.Integer, db.ForeignKey('user.id'))

class Follower(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user = db.Column(db.Integer, db.ForeignKey('user.id'))
    problem = db.Column(db.Integer, db.ForeignKey('problem.id'))
    date = Column(DateTime, default=datetime.datetime.utcnow)

class Comentario(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user = db.Column(db.Integer, db.ForeignKey('user.id'))
    problem = db.Column(db.Integer, db.ForeignKey('problem.id'))
    text = db.Column(db.String(40))
    date = Column(DateTime, default=datetime.datetime.utcnow)