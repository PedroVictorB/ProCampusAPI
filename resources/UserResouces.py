from flask import request, jsonify, Blueprint
from models.Banco import db, User

__author__ = 'pedro'

user_route = Blueprint('user', __name__)

# Rotas do usuario
@user_route.route('/user')
def user():
    return 'Usuarios'


@user_route.route('/user/create', methods=['POST'])
def createUser():
    if request.method == 'POST':
        u = User(
            name=request.form.get('name'),
            email=request.form.get('email'),
            matricula=request.form.get('matricula')
        )
        db.session.add(u)
        db.session.commit()
        return jsonify({'id': u.id})

    return jsonify({'error': 'not created'})


@user_route.route('/user/<int:id>')
def readUser(id):
    u = User.query.get(id)
    if u == None:
        return jsonify({'error': 'user not found'})
    else:
        return jsonify({'id': u.id, 'name': u.name, 'email': u.email, 'date': str(u.date), 'matricula':u.matricula})

@user_route.route('/user/matricula/<string:matricula>')
def readMatriculaUser(matricula):
    u = User.query.filter_by(matricula=matricula).first()
    if u == None:
        return jsonify({'error': 'user not found'})
    else:
        return jsonify({'id': u.id, 'name': u.name, 'email': u.email, 'date': str(u.date), 'matricula':u.matricula})


@user_route.route('/user/readAll')
def readAllUser():
    users = User.query.all()
    dict_user = []
    if users == None:
        return jsonify({'error': 'no users'})
    for u in users:
        dict_user.append({'id': u.id, 'name': u.name, 'email': u.email, 'date': str(u.date), 'matricula':u.matricula})

    return jsonify(users=dict_user)


@user_route.route('/user/update')
def updateUser():
    return 'Create'


@user_route.route('/user/delete')
def deleteUser():
    return 'Create'