import StringIO
import os
from flask import request, jsonify, Blueprint, send_file
import io
from werkzeug.utils import secure_filename
from models.Banco import db, Teste

__author__ = 'pedro'

test_route = Blueprint('test', __name__)

# Rotas do usuario
@test_route.route('/test/insert', methods=['POST'])
def createTest():
    #request.files['image'].save('/tmp')
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join('/temp/', filename))
    #str = StringIO.StringIO()
    #str.write(image)
    #str.seek(0)
    #f = open(image, 'rb').read()
    #bin_file = StringIO.StringIO(image.read())
    # if image:
    #     t = Teste(
    #         image = buffer(image.read())
    #     )
    #     db.session.add(t)
    #     db.session.commit()
    #     return jsonify({'id': t.id})
    return jsonify({'error': 'Deu ruim'})

@test_route.route('/test/<int:id>')
def readTest(id):
    t = Teste.query.get(id)
    if t == None:
        return jsonify({'error': 'image not found'})
    else:
        return jsonify({'id': t.id, 'image': t.image})