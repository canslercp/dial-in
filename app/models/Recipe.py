from mongoengine import Document
from mongoengine import *

class Recipe(Document):
  amountCoffee = IntField(required=True, trim=True)
  amountWater = IntField(required=True, trim=True)
  grindSize = IntField(required=True, trim=True)
  waterTemp = IntField(trim=True)
  brewer = StringField()
