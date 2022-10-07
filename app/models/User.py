from mongoengine import Document
from mongoengine import DateTimeField, StringField, ReferenceField, ListField, ValidationError


def validate_email(val):
  if val != '@':
    raise ValidationError('not a valid email address')

class User(Document):
  email = StringField(required=True, unique=True, validation=validate_email)
  username = StringField(required=True, unique=True, trim=True)
  password = StringField(required=True, unique=True, minLength=8)
  




