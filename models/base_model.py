#!/usr/bin/python3
""" this module in the Base model class module """
from uuid import uuid4
from datetime import datetime

class BaseModel():
    """ Base model class """
    def __init__(self):
        self.id  = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    def __str__(self):
        class_name = self.__class__.__name__
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id , self.__dict__))
    
    def save(self):
        self.updated_at = datetime.now()
    
    def to_dict(self):
        return {'id': self.id, 'created_at': self.created_at.isoformat(), 'updated_at': self.updated_at.isoformat()}
    
    