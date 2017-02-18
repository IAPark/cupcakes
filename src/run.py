from flask import Flask, jsonify, request
import flask_cors
from flask_cors import CORS, cross_origin
from recipe import Recipe

app = Flask(__name__)
CORS(app)

@app.route('/cake', methods=['POST'])
def addCake():
    json = request.get_json()
    recipe = Recipe(name=json['name'], category=1)
    recipe.save()
    return jsonify({'status': 'success', 'recipe': recipe.get_dict()})

@app.route('/cakes', methods=['get'])
def getCakes():
    cakes = []
    for cake in Recipe.select().where(Recipe.category==1):
        cakes.append(cake.get_dict())
    return jsonify({'status': 'success', 'cake': cakes})


if __name__ == "__main__":
    app.run(debug=True)