#!/usr/bin/python3
"""c"""
import json
import os
import sys
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage:
    """CC"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """c"""
        return self.__objects

    def new(self, obj):
        """c"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ coment """
        new_dict = {o: self.__objects[o].to_dict()
                    for o in self.__objects.keys()}
        with open(self.__file_path, mode="w") as file:
            json.dump(new_dict, file)

    def reload(self):
        """ coment """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, mode="r") as file:
                for key, value in (json.loads(file.read())).items():
                    value = getattr(
                        sys.modules[__name__], key.split(".")[0])(**value)
                    self.__objects[key] = value
