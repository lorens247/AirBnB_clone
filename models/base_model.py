#!/usr/bin/python3
"""Defines base class BaseModel"""

import uuid
from datetime import datetime
from models import storage

class BaseModel:
    """Defined a super class that handles objects"""
    def __init__(self, *args, **kwargs):
        """Initializes the object"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == 'created_at' or key == 'updated_at':
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Prints class name, id, and dictionary of using class"""
        return "[{}] ({}) {}"\
            .format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute
        update_at var to current time"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing all
        key/value pairs of an instance"""
        obj_dict = self.__dict__.copy()
        for key, value in self.__dict__.items():
            if key == 'created_at' or key == 'updated_at':
                obj_dict[key] = value.isoformat()

        obj_dict['__class__'] = type(self).__name__

        return obj_dict
