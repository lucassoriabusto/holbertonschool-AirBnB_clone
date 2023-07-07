#!/usr/bin/python3
"""
Unittest for User class
"""
import unittest
from models.user import User
from datetime import datetime


class TestUser(unittest.TestCase):

    def test_create_class(self):
        b1 = User()
        self.assertIsInstance(b1, User)

    def test_id_instance(self):
        b1 = User()
        self.assertIsInstance(b1.id, str)

    def test_created_at_instance(self):
        b1 = User()
        self.assertIsInstance(b1.created_at, datetime)

    def test_updated_at_instance(self):
        b1 = User()
        self.assertIsInstance(b1.updated_at, datetime)

    def test_save(self):
        b1 = User()
        old_datetime = b1.updated_at
        b1.save()
        new_datetime = b1.updated_at
        self.assertNotEqual(old_datetime, new_datetime)

    def test_dict(self):
        b1 = User()
        new_dict = b1.to_dict()
        self.assertIsInstance(new_dict, dict)

    def test_to_dict_contains_all_attributes(self):
        b1 = User()
        result = b1.to_dict()
        self.assertIn("id", result)
        self.assertIn("created_at", result)
        self.assertIn("updated_at", result)

    def test_str(self):
        b1 = User()
        str_rep = str(b1)
        self.assertIn(b1.__class__.__name__, str_rep)
        self.assertIn(b1.id, str_rep)


if __name__ == "__main__":
    unittest.main()
