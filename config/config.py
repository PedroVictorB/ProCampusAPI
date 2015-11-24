__author__ = 'pedro'

import os

DEBUG = True

basedir = os.path.abspath(os.path.dirname(__file__))

if os.environ.get('DATBASE_URL') is None:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:admin@localhost/procampus'
else:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']