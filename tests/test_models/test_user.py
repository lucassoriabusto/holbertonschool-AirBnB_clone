#!/usr/bin/python3
"""
Unittest for User class
"""
import unittest
from models.user import User
from datetime import datetime


class TestUser(unittest.TestCase):

    def test_create_class(self):
        u1 = User()
        self.assertIsInstance(u1, User)

    def test_create_email(self):
        u1 = User()
        u1.email = "pepito89@hotmail.com"
        self.assertAlmostEqual(u1.email, "pepito89@hotmail.com")
        self.assertIsInstance(u1.email, str)

    def test_create_password(self):
        u1 = User()
        u1.password = "password"
        self.assertAlmostEqual(u1.password, "password")
        self.assertIsInstance(u1.password, str)

    def test_create_first_name(self):
        u1 = User()
        u1.first_name = "Pepe"
        self.assertAlmostEqual(u1.first_name, "Pepe")
        self.assertIsInstance(u1.first_name, str)

    def test_create_last_name(self):
        u1 = User()
        u1.last_name = "Noches"
        self.assertAlmostEqual(u1.last_name, "Noches")
        self.assertIsInstance(u1.last_name, str)


if __name__ == "__main__":
    unittest.main()
