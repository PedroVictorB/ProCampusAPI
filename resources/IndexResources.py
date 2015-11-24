__author__ = 'pedro'

from flask import Blueprint

index_route = Blueprint('index', __name__)

# index da API
@index_route.route('/')
def index():
    return 'Bem vindo a API Pro Campus!'