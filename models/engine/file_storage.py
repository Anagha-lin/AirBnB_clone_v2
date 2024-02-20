#!/usr/bin/python3
""" FileStorage class module """
import json
from models.base_model import BaseModel

class FileStorage:
    """ FileStorage class """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """ Returns the dictionary __objects """
        if cls:
            return {key: obj for key, obj in self.__objects.items()
                    if isinstance(obj, cls)}
        return self.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id """
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """ Serializes __objects to the JSON file (path: __file_path) """
        obj_dict = {}
        for key, value in self.__objects.items():
            obj_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="utf-8") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """ Deserializes the JSON file to __objects """
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    cls_name, obj_id = key.split(".")
                    cls = eval(cls_name)
                    self.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """ Deletes an object from __objects """
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            del self.__objects[key]


