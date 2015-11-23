import datetime
from flask import Flask, request, jsonify
from models.Banco import Problem, db, heroku
from models.Banco import User

app = Flask(__name__)

#index da API
@app.route('/')
def index():
    return 'Bem vindo a API Pro Campus!'


#Rotas do usuario
@app.route('/user')
def user():
    return 'Usuarios'

@app.route('/user/create', methods=['POST'])
def createUser():
    if request.method == 'POST':
        u = User(
            name = request.form.get('name'),
            email = request.form.get('email')
        )
        db.session.add(u)
        db.session.commit()
        return jsonify({'id':u.id})

    return jsonify({'error':'not created'})

@app.route('/user/<int:id>')
def readUser(id):
    u = User.query.get(id)
    if u == None:
        return jsonify({'error':'user not found'})
    else:
        return jsonify({'id':u.id, 'name':u.name, 'email':u.email, 'date':str(u.date)})

@app.route('/user/readAll')
def readAllUser():
    users = User.query.all()
    dict_user = []
    if users == None:
        return jsonify({'error':'no users'})
    for u in users:
        dict_user.append({'id':u.id, 'name':u.name, 'email':u.email, 'date':str(u.date)})

    return jsonify(users=dict_user)

@app.route('/user/update')
def updateUser():
    return 'Create'

@app.route('/user/delete')
def deleteUser():
    return 'Create'


#Rotas dos problemas
@app.route('/problem')
def problem():
    return 'Marcadores'

@app.route('/problem/create', methods=['GET', 'POST'])
def createProblem():
    if request.method == 'POST':
        p = Problem(
            title = request.form.get('title'),
            category = request.form.get('category'),
            description = request.form.get('description'),
            latitude = request.form.get('latitude'),
            longitude = request.form.get('longitude'),
            user = request.form.get('user'),
        )
        db.session.add(p)
        db.session.commit()
        return jsonify({'id':p.id})

@app.route('/problem/readAll')
def readAllProblem():
    problems = Problem.query.all()
    list = []
    if problems == None:
        return jsonify({'error':'problems not found'})
    else:
        for p in problems:
            list.append({'id':p.id, 'title':p.title, 'category':p.category, 'date':str(p.date), 'description':p.description, 'latitude':p.latitude, 'longitude':p.longitude, 'user':p.user})
        return jsonify(problems=list)

@app.route('/problem/read/<int:id>')
def readProblem(id):
    p = Problem.query.get(id)
    if p == None:
        return jsonify({'error':'problem not found'})
    else:
        return jsonify({'id':p.id, 'title':p.title, 'category':p.category, 'date':str(p.date), 'description':p.description, 'latitude':p.latitude, 'longitude':p.longitude, 'user':p.user})

@app.route('/problem/user/<int:id>')
def userProblem(id):
    problems = Problem.query.all()
    list = []
    if problems == None:
        return jsonify({'error':'no problems'})
    for p in problems:
        if p.user == id:
            list.append({'id':p.id, 'title':p.title, 'category':p.category, 'date':str(p.date), 'description':p.description, 'latitude':p.latitude, 'longitude':p.longitude, 'user':p.user})
    return jsonify(problems=list)

@app.route('/problem/update')
def updateProblem():
    return 'Update'

@app.route('/problem/delete')
def deleteProblem():
    return 'Delete'

#rotas dos comentarios


if __name__ == '__main__':
    app.run()
