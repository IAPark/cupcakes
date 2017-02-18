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
    starting_with =  ForeignKeyField(Recipe, related_name='pairings')
    ending_with =  ForeignKeyField(Recipe, related_name='pairingsResults')
    def get_dict(self):
        return {
            'starting_with': self.starting_with.get_dict(),
            'ending_with': self.ending_with.get_dict(),
            'why': self.why,
            'id': self.id
        }

class Ingredient(BaseModel):
    name = CharField()

class IngredientUsed(BaseModel):
    recipe = ForeignKeyField(Recipe, related_name='ingredients')
    ingredient = ForeignKeyField(Ingredient, related_name='uses')
    amount = IntegerField()
    unit = CharField()


db.create_tables([Recipe, Ingredient, IngredientUsed, Pairing], safe=True)