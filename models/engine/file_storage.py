#!/usr/bin/python3
"""A Module for FileStorage class"""

import json
import os


class FileStorage:
    """A FileStorage Class :
    Serializes instances to a JSON file and deserializes
    JSON file to instances.

    Attributes:
        __file_path (str): a path to a JSON file where the object
            representations will be saved and reloaded from.
        __objects (dict): a dictionary containing all object
            representations.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """A method that returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """A method that sets in __objects the obj with key <obj class name>.id

        Args:
            obj (obj): an object of a given class
        """

        key = type(obj).__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """A method that serializes __objects to the JSON file
        (path: __file_path)"""

        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, "w", encoding='utf-8') as f:
            json.dump(new_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        from models import base_model

        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                reloaded_objects = {}
                reloaded_objects = json.load(file)
                for key, value in reloaded_objects.items():
                    class_name = value['__class__']
                    cls = getattr(base_model, class_name)
                    obj = cls(**value)
                    self.__objects[key] = obj
