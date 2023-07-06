#!/usr/bin/python3
"""Module for FileStorage"""
import json
import os


class FileStorage:
    """Class FileStorage :
    Serializes instances to a JSON file and deserializes
    JSON file to instance.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = type(obj).__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, "w", encoding='utf-8') as f:
            json.dump(new_dict, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        from models import base_model
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as input_file:
                jsoned_obj = {}
                jsoned_obj = json.load(input_file)
                for key, value in jsoned_obj.items():
                    class_name = value['__class__']
                    class_obj = getattr(base_model, class_name)
                    obj = class_obj(**value)
                    self.__objects[key] = obj
