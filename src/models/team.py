#!/usr/bin/python3
"""a module defining team heads of different locations as a type of user"""
import mongoengine
from user import User
from booking import Booking

class SAFI_team_lead(mongoengine.EmbeddedDocument, User):
    """class defining attributes
    of a SAFI_team_lead who dispatches cleaning teams"""
    
    name = mongoengine.StringField(required=True)
    second_name = mongoengine.StringField(required=True)
    working_hours = mongoengine.DateTimeField(required=True)

    bookings = mongoengine.EmbeddedDocumentListField(Booking)

    meta = {
        'db_alias': 'core',
        'collections': 'teams'
    }

     def __init__(self, *args, **kwargs):
        """initialization"""
        super().__init__(*args, **kwargs)