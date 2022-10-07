from mongoengine import Document
from mongoengine import DateTimeField, StringField, IntField, ReferenceField, ListField, ValidationError
from .Recipe import Recipe 
from .User import User

class Coffee(Document):
  roaster = StringField(required=True, trim=True)
  name = StringField(required=True, trim=True)
  originCountry = StringField()
  regionCountry = StringField(trim=True)
  elevationGrown = IntField(trim=True)
  processMethod = StringField()
  roastLevel = StringField()
  roastDate = DateTimeField()

  user = ReferenceField(User)
  recipes = ReferenceField(Recipe)

