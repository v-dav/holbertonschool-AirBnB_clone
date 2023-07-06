#!/usr/bin/python3
"""Module for BaseModel"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Class Base : The "base” of all other classes"""

    def __init__(self, *args, **kwargs):
        """Initialize a new Base

        Args:
            id (int): The identity of the new Base
            *args (ints): New attribute values
            **kwargs (dict): New attribute values
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            for k, v in kwargs.items():
                if k == "updated_at" or k == "created_at":
                    v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                if k != '__class__':
                    setattr(self, k, v)

    def __str__(self):
        """Return description of the class"""
        return ("[{}] ({}) {}".format(type(self).__name__,
                self.id, self.__dict__))

    def save(self):
        """Updates attribute with the current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns the dictionary representation with modified keywords"""
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict
