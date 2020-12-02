from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify, request, Flask, render_template
from app import app
from app import mongo
from classe_musica import Musica

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/add', methods=['POST'])
def add_musica():

    _json = request.json
    musica = Musica(_json["musica"], _json["autor"], _json["genero"])

    if musica.musica and musica.autor and musica.genero and request.method == 'POST':

        id = mongo.db.musica.insert(
            {'musica': musica.musica, 'autor': musica.autor, 'genero': musica.genero})

        resp = jsonify("musica adicionada")

        resp.status_code = 200

        return resp


@app.route('/musica')
def listar_musica():
    musica = mongo.db.musica.find()
    resp = dumps(musica)
    return resp


@app.route('/musica/<id>')
def pesquisar_musica(id):
    musica = mongo.db.musica.find_one({'_id': ObjectId(id)})
    resp = dumps(musica)
    return resp


@app.route('/delete/<id>', methods=['DELETE'])
def delete_musica(id):
    mongo.db.musica.delete_one({'_id': ObjectId(id)})
    resp = jsonify("musica deletada")

    resp.status_code = 200

    return resp


@app.route('/update/<id>', methods=['PUT'])
def update_musica(id):
    _id = id
    _json = request.json
    musica = Musica(_json["musica"], _json["autor"], _json["genero"])


    if musica.musica and musica.autor and musica.genero and _id and request.method == 'PUT':

        mongo.db.musica.update_one({'_id': ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(
            _id)}, {'$set': {'musica': musica.musica, 'autor': musica.autor, 'genero': musica.genero}})

        resp = jsonify("musica atualizada")

        resp.status_code = 200

        return resp


if __name__ == "__main__":
    app.run(debug=True)
