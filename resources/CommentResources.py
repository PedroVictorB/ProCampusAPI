from flask import Blueprint, request, jsonify
from models.Banco import Comentario, db

__author__ = 'pedro'

comment_route = Blueprint('comment', __name__)

# rotas dos comentarios
@comment_route.route('/comment')
def comment():
    return 'Comentarios'


@comment_route.route('/comment/create', methods=['GET', 'POST'])
def createComment():
    if request.method == 'POST':
        c = Comentario(
            user=request.form.get('user'),
            problem=request.form.get('problem'),
            text=request.form.get('text')
        )
        db.session.add(c)
        db.session.commit()
        return jsonify({'id': c.id})


@comment_route.route('/comment/readAll')
def readAllComment():
    comments = Comentario.query.all()
    list = []
    if comments == None:
        return jsonify({'error': 'comments not found'})
    else:
        for c in comments:
            list.append({'id': c.id, 'user': c.user, 'problem': c.problem, 'date': str(c.date), 'text': c.text})
        return jsonify(comments=list)


@comment_route.route('/comment/read/<int:id>')
def readComment(id):
    c = Comentario.query.get(id)
    if c == None:
        return jsonify({'error': 'comment not found'})
    else:
        return jsonify({'id': c.id, 'user': c.user, 'problem': c.problem, 'date': str(c.date), 'text': c.text})


@comment_route.route('/comment/user/<int:id>')
def userComment(id):
    comments = Comentario.query.all()
    list = []
    if comments == None:
        return jsonify({'error': 'no comments'})
    for c in comments:
        if c.user == id:
            list.append({'id': c.id, 'user': c.user, 'problem': c.problem, 'date': str(c.date), 'text': c.text})
    return jsonify(problems=list)


@comment_route.route('/comment/update')
def updateComment():
    return 'Update'


@comment_route.route('/comment/delete')
def deleteComment():
    return 'Delete'