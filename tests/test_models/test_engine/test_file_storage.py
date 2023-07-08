#!/usr/bin/python3
"""
Unittest for FileStorage class
"""
import unittest
import os
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """ tests for the FileStorage class """

    def setUp(self) -> None:
        """ setup method """
        self.storage = FileStorage()
        self.path = "file.json"

    def tearDown(self) -> None:
        """ teardown method """
        if os.path.exists(self.path):
            os.remove(self.path)

    def test_all(self):
        """ test all method """
        self.assertAlmostEqual(self.storage.all(), {})
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        """ test new method """
        obj = BaseModel()
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.assertAlmostEqual(len(self.storage.all()), 1)
        self.assertAlmostEqual(key in self.storage.all(), True)

    def test_save(self):
        """ test save method V1"""
        obj = BaseModel()
        self.storage.save()
        self.assertAlmostEqual(os.path.exists(self.path), True)
        with open(self.path, mode="r") as file:
            text = json.load(file)
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.assertIn(key, text)

    def test_save_2(self):
        """ Test save method V2"""
        b1 = BaseModel()
        old_datetime = b1.updated_at
        self.storage.save()
        with open(self.path, mode="r") as file:
            text_1 = json.load(file)
        b1.save()
        new_datetime = b1.updated_at
        with open(self.path, mode="r") as file:
            text_2 = json.load(file)
        self.assertNotEqual(old_datetime, new_datetime)
        self.assertNotEqual(text_1, text_2)

    def test_reload(self):
        """ test reload method V1"""
        obj = BaseModel()
        self.storage.save()
        dict = self.storage.all()
        self.assertEqual(len(dict), 2)
        for key in dict.keys():
            self.assertTrue(isinstance(dict[key], BaseModel))

    def test_reload_2(self):
        """ test reload method V2 """
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

    def test_obj_is_dict(self):
        """ test to check if the obj is a dict"""
        self.assertAlmostEqual(type(self.storage._FileStorage__objects), dict)

    def test_path_contais_str(self):
        """ test to check if the path is a str"""
        self.assertAlmostEqual(type(self.storage._FileStorage__file_path), str)

    def test_file_path(self):
        """ test to check if the file path is correct"""
        self.assertAlmostEqual(
            self.storage._FileStorage__file_path, "file.json")


if __name__ == "__main__":
    unittest.main()
