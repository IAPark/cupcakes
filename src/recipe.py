from db import BaseModel, db 
from peewee import *


class Recipe(BaseModel):
    name = CharField()
    category = IntegerField()
    def get_dict(self):
        return {
            'name': self.name,
            'category': self.category,
            'id': self.id
        }

class Pairing(BaseModel):
    why = CharField()
    startingWith =  ForeignKeyField(Recipe, related_name='pairings')
    endingWith =  ForeignKeyField(Recipe, related_name='pairingsResults')

class Ingredient(BaseModel):
    name = CharField()

class IngredientUsed(BaseModel):
    recipe = ForeignKeyField(Recipe, related_name='ingredients')
    ingredient = ForeignKeyField(Ingredient, related_name='uses')
    amount = IntegerField()
    unit = CharField()


db.create_tables([Recipe, Ingredient, IngredientUsed, Pairing], safe=True)