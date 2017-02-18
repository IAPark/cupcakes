from peewee import *

db = SqliteDatabase('cupcake.db')

class BaseModel(Model):
    class Meta:
        database = db

db.connect()

