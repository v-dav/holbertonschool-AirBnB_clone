#!/usr/bin/python3
"""A Module for BaseModel class"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """A BaseModel Class : The "base” of all other classes"""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel object with id and
        time it was created and updated by default or with a
        dictionary containing attributes.

        Args:
            *args (tuple): New attribute values
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
        """Returns human-readable description of the object"""

        return ("[{}] ({}) {}".format(type(self).__name__,
                self.id, self.__dict__))

    def save(self):
        """Updates attributes with the current datetime and
        writes the object as JSON representation in a file"""

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns the dictionary representation with additional
        and formatted attrbutes"""

        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict
