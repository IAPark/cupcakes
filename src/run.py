from flask import Flask, jsonify, request
import flask_cors
from flask_cors import CORS, cross_origin
from recipe import Recipe, Pairing
from functools import partial

app = Flask(__name__)
CORS(app)

def addRecipies(category):
    json = request.get_json()
    recipe = Recipe(name=json['name'], category=category)
    recipe.save()
    return jsonify({'status': 'success', 'recipe': recipe.get_dict()})

def getRecipies(category):
    cakes = []
    for cake in Recipe.select().where(Recipe.category==category):
        cakes.append(cake.get_dict())
    return jsonify({'status': 'success', 'recipes': cakes})


@app.route('/cake', methods=['POST'])
def addCake():
    return addRecipies(1)

@app.route('/cakes', methods=['get'])
def getCakes():
    return getRecipies(1)


@app.route('/icing', methods=['POST'])
def addIcing():
    return addRecipies(2)

@app.route('/icings', methods=['get'])
def getIcings():
    return getRecipies(2)

@app.route('/pairings')
def getPairings():
    pairings = []
    for pairing in Pairing.select():
        pairings.append(paring.get_dict())
    return jsonify({'status': 'success', 'pairings': pairings})

@app.route('/pairing', methods=['POST'])
def addPairing():
    json = request.get_json()
    pairing = Pairing(why=[json['why'], starting_with=json['starting_with'])



if __name__ == "__main__":
    app.run(debug=True)