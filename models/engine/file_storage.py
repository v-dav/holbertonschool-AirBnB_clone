#!/usr/bin/python3
"""A module with File Storage class"""

import json
import os


class FileStorage:
    """A class that serializes instances to a JSON file
    and deserializes JSON file to instances.

    Attributes:
        __file_path (str): path to JSON file
        __objects (dict): dictionary that stores all objects"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary objects"""

        return self.__objects

    def new(self, obj):
        """Sets new objects in __objects"""

        from base_model import BaseModel

        key = str(obj.__class__.__name__) + "." + str(obj.id)
        FileStorage.__objects[key] = obj.to_dict()

    def save(self):
        """Serializes __objects to the JSON file"""

        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(FileStorage.__objects, file)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised) """

        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                FileStorage.__objects = json.load(file)
