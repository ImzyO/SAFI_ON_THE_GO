#!/usr/bin/python3
"""module defines a class user 
with different user types"""

from base_model import BaseModel
import mongoengine

class User(mongoengine.EmbeddedDocument, BaseModel):
    """user class with attributes of user
     relating to car woner, dealership, 
     rentals, office"""
    name = mongoengine.StringField(required=True)
    email = mongoengine.StringField(required=True)
    password = None
    phone_number = mongoengine.IntField(required=True)
    country = mongoengine.StringField(required=True)
    city = mongoengine.StringField(required=True)
    town = mongoengine.StringField(required=True)
    address = mongoengine.StringField(required=True)

    """db_alias=what data base connection to 
    use and collections is similar to tablename"""

     meta = {
        'db_alias': 'core',
        'collections': 'users',
        'allow_inheritance': True
    }

     def __init__(self, *args, **kwargs):
        """initialization"""
        # inheritance from BaseModel
        super().__init__(*args, **kwargs)