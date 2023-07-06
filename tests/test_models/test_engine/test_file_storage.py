#!/usr/bin/python3
"""
Unittest for BaseModel class
"""
import unittest
import os
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime


class TestBaseModel(unittest.TestCase):

    def setUp(self) -> None:
        self.storage = FileStorage()
        self.path = "file.json"

    def tearDown(self) -> None:
        if os.path.exists(self.path):
            os.remove(self.path)

    def test_all(self):
        self.assertAlmostEqual(self.storage.all(), {})

    def test_create_new(self):
        obj = BaseModel()
        self.storage.new(obj)
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.assertAlmostEqual(key in self.storage.all(), True)

    def test_save(self):
        obj = BaseModel()
        self.storage.save()
        self.assertAlmostEqual(os.path.exists(self.path), True)
        with open(self.path, mode="r") as file:
            text = json.dumps(file.read())
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.assertAlmostEqual(key in text, True)

    def test_reload(self):
        obj = BaseModel()
        self.storage.save()
        self.storage.reload()
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.assertAlmostEqual(key in self.storage.all(), True)

    def test_file_is_str(self):
        self.assertAlmostEqual(type(self.storage._FileStorage__objects), dict)

    def test_storage_contais_dict(self):
        self.assertAlmostEqual(type(self.storage._FileStorage__file_path), str)

    def test_file_path(self):
        self.assertAlmostEqual(
            self.storage._FileStorage__file_path, "file.json")


if __name__ == "__main__":
    unittest.main()
