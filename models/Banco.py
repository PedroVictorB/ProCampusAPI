from flask.ext.heroku import Heroku

__author__ = 'pedro'

import datetime
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import DateTime, Column
from flask import Flask
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
import os

app = Flask(__name__)


DEBUG = True

basedir = os.path.abspath(os.path.dirname(__file__))

if os.environ.get('DATABASE_URL') is None:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:admin@localhost/procampus'
else:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
heroku = Heroku(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(40))
    email = db.Column(db.String(80), unique=True)
    matricula = db.Column(db.String(15), unique=True)
    date = Column(DateTime, default=datetime.datetime.utcnow)


class Problem(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(40))
    category = db.Column(db.String(40))
    description = db.Column(db.String(120))
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
    text = db.Column(db.String(120))
    date = Column(DateTime, default=datetime.datetime.utcnow)

if __name__ == '__main__':
    manager.run()