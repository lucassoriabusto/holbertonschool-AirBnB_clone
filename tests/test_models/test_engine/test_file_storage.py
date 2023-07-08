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
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        obj = BaseModel()
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.assertAlmostEqual(len(self.storage.all()), 1)
        self.assertAlmostEqual(key in self.storage.all(), True)

    def test_save(self):
        obj = BaseModel()
        self.storage.save()
        self.assertAlmostEqual(os.path.exists(self.path), True)
        with open(self.path, mode="r") as file:
            text = json.load(file)
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.assertIn(key, text)

    def test_reload(self):
        obj = BaseModel()
        self.storage.save()
        dict = self.storage.all()
        self.assertEqual(len(dict), 2)
        for key in dict.keys():
            self.assertTrue(isinstance(dict[key], BaseModel))

    def test_reload_2(self):
        """ Test reload method """
        my_model = BaseModel()
        self.storage.new(my_model)
        self.storage.save()
        with open(self.path, "r") as file:
            data = json.load(file)
        data["BaseModel.1234"] = {"id": "1234",
                                  "__class__": "BaseModel", "name": "test",
                                  "created_at": "2023-07-06T14:19:45.911051",
                                  "updated_at": "2023-07-06T14:19:45.911061"}
        with open(self.path, "w") as file:
            json.dump(data, file)
        self.storage.reload()
        self.assertIn("BaseModel.1234", self.storage.all())
        obj = self.storage.all()["BaseModel.1234"]
        self.assertEqual(obj.id, "1234")
        self.assertEqual(obj.name, "test")

    def test_file_is_dict(self):
        self.assertAlmostEqual(type(self.storage._FileStorage__objects), dict)

    def test_storage_contais_str(self):
        self.assertAlmostEqual(type(self.storage._FileStorage__file_path), str)

    def test_file_path(self):
        self.assertAlmostEqual(
            self.storage._FileStorage__file_path, "file.json")


if __name__ == "__main__":
    unittest.main()
