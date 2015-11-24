from flask import Blueprint, request, jsonify
from models.Banco import Follower, db

__author__ = 'pedro'

follower_route = Blueprint('follower', __name__)

# Rotas dos seguidores
@follower_route.route('/follower')
def follower():
    return 'Comentarios'


@follower_route.route('/follower/create', methods=['GET', 'POST'])
def createFollower():
    if request.method == 'POST':
        f = Follower(
            user=request.form.get('user'),
            problem=request.form.get('problem')
        )
        db.session.add(f)
        db.session.commit()
        return jsonify({'id': f.id})


@follower_route.route('/follower/readAll')
def readAllFollower():
    followers = Follower.query.all()
    list = []
    if followers == None:
        return jsonify({'error': 'followers not found'})
    else:
        for f in followers:
            list.append({'id': f.id, 'user': f.user, 'problem': f.problem})
        return jsonify(followers=list)


@follower_route.route('/follower/read/<int:id>')
def readFollower(id):
    f = Follower.query.get(id)
    if f == None:
        return jsonify({'error': 'follow not found'})
    else:
        return jsonify({'id': f.id, 'user': f.user, 'problem': f.problem})


@follower_route.route('/follower/user/<int:id>')
def userFollower(id):
    followers = Follower.query.all()
    list = []
    if followers == None:
        return jsonify({'error': 'no followers'})
    for f in followers:
        if f.user == id:
            list.append({'id': f.id, 'user': f.user, 'problem': f.problem})
    return jsonify(problems=list)


@follower_route.route('/follower/update')
def updateFollower():
    return 'Update'


@follower_route.route('/follower/delete')
def deleteFollower():
    return 'Delete'