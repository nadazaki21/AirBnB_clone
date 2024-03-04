#!/usr/bin/python3
""" this module in the Base model class module """
from uuid import uuid4
from datetime import datetime

class BaseModel():
    """ Base model class """
    def __init__(self, *args, **kwargs):
        if kwargs != {}:
            for key, value in kwargs.items():
                if key == "__class__":
                    pass
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                else:
                    setattr(self, key, value)
        else:
            self.id  = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        class_name = self.__class__.__name__
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id , self.__dict__))
    
    def save(self):
        self.updated_at = datetime.now()
    
    def to_dict(self):
        # Get all instance attributes
        obj_dict = self.__dict__.copy()  #copy is used to create a copy, without it we'd create a refrence

        # Add __class__ attribute
        obj_dict['__class__'] = self.__class__.__name__

        # Convert created_at and updated_at to ISO format strings
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()

        return obj_dict
    
    