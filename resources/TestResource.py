import base64
from flask import request, jsonify, Blueprint
from models.Banco import db, Teste

__author__ = 'pedro'

test_route = Blueprint('test', __name__)

# Rotas do usuario
@test_route.route('/test/insert', methods=['POST'])
def createTest():
    if request.method == "POST":
        photo = request.files['image']
        file = photo.read()
        print(file)
        t = Teste(
            image=file
        )
        db.session.add(t)
        db.session.commit()
        return jsonify({'id': t.id})
    return jsonify({'error': 'Deu ruim'})

@test_route.route('/test/<int:id>')
def readTest(id):
    t = Teste.query.get(id)
    txt = base64.encodestring(t.image)
    if t == None:
        return jsonify({'error': 'image not found'})
    else:
        return jsonify({'id': t.id, 'image': txt})