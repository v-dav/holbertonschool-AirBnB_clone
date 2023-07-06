#!/usr/bin/python3

"""The base class of all our models"""

import uuid
from datetime import datetime


class BaseModel:
    """Defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """The class constructor method for the class instance.

        Args:
            args (tuple):
            kwargs (dict): a dictionary with instance attribute names and
                values
        """

        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """Public instance method for human readable
        representation of the instance.

        Return: a string"""

        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Public instance method that updates
        the public instance attribute."""

        self.updated_at = datetime.now()

    def to_dict(self):
        """Public instance method that updates and returns
        a dictionary containing all keys/values of __dict__ of the instance.

        Returns: a dictionary."""

        my_dict = self.__dict__
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict
