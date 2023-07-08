#!/usr/bin/python3
"""
Unittest for User class
"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):

    def test_create_class(self):
        u1 = User()
        self.assertIsInstance(u1, User)
        self.assertTrue(hasattr(u1, "email"))
        self.assertTrue(hasattr(u1, "password"))
        self.assertTrue(hasattr(u1, "first_name"))
        self.assertTrue(hasattr(u1, "last_name"))
        
    def test_empty_attributes(self):
        u1 = User()
        self.assertAlmostEqual(u1.email, "")
        self.assertAlmostEqual(u1.password, "")
        self.assertAlmostEqual(u1.first_name, "")
        self.assertAlmostEqual(u1.last_name, "")


if __name__ == "__main__":
    unittest.main()
