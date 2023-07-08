#!/usr/bin/python3
"""
Unittest for State class
"""
import unittest
from models.state import State


class TestState(unittest.TestCase):

    def test_create_class(self):
        u1 = State()
        self.assertIsInstance(u1, State)
        self.assertTrue(hasattr(u1, "name"))
        
    def test_empty_attributes(self):
        u1 = State()
        self.assertAlmostEqual(u1.name, "")


if __name__ == "__main__":
    unittest.main()