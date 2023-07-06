#!/usr/bin/python3
"""c"""


class FileStorage:
    """CC"""
    __file_path = "file.json"
    __objects = {}

    @staticmethod
    def all(self):
        """c"""
        return FileStorage.__objects

    def new(self, obj):
        """c"""
        key = obj.__class.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj
