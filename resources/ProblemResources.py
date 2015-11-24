__author__ = 'pedro'

from models.Banco import Problem, db
from flask import request, jsonify, Blueprint

problem_route = Blueprint('problem', __name__)

# Rotas dos problemas
@problem_route.route('/problem')
def problem():
    return 'Marcadores'


@problem_route.route('/problem/create', methods=['GET', 'POST'])
def createProblem():
    if request.method == 'POST':
        p = Problem(
            title=request.form.get('title'),
            category=request.form.get('category'),
            description=request.form.get('description'),
            latitude=request.form.get('latitude'),
            longitude=request.form.get('longitude'),
            user=request.form.get('user'),
        )
        db.session.add(p)
        db.session.commit()
        return jsonify({'id': p.id})


@problem_route.route('/problem/readAll')
def readAllProblem():
    problems = Problem.query.all()
    list = []
    if problems == None:
        return jsonify({'error': 'problems not found'})
    else:
        for p in problems:
            list.append({'id': p.id, 'title': p.title, 'category': p.category, 'date': str(p.date),
                         'description': p.description, 'latitude': p.latitude, 'longitude': p.longitude,
                         'user': p.user})
        return jsonify(problems=list)


@problem_route.route('/problem/read/<int:id>')
def readProblem(id):
    p = Problem.query.get(id)
    if p == None:
        return jsonify({'error': 'problem not found'})
    else:
        return jsonify(
            {'id': p.id, 'title': p.title, 'category': p.category, 'date': str(p.date), 'description': p.description,
             'latitude': p.latitude, 'longitude': p.longitude, 'user': p.user})


@problem_route.route('/problem/user/<int:id>')
def userProblem(id):
    problems = Problem.query.all()
    list = []
    if problems == None:
        return jsonify({'error': 'no problems'})
    for p in problems:
        if p.user == id:
            list.append({'id': p.id, 'title': p.title, 'category': p.category, 'date': str(p.date),
                         'description': p.description, 'latitude': p.latitude, 'longitude': p.longitude,
                         'user': p.user})
    return jsonify(problems=list)


@problem_route.route('/problem/update')
def updateProblem():
    return 'Update'


@problem_route.route('/problem/delete')
def deleteProblem():
    return 'Delete'

