#!/usr/bin/python3
"""
Unittest for City class
"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):

    def test_create_class(self):
        c1 = City()
        self.assertIsInstance(c1, City)
        self.assertTrue(hasattr(c1, "state_id"))
        self.assertTrue(hasattr(c1, "name"))
        
    def test_empty_attributes(self):
        c1 = City()
        self.assertAlmostEqual(c1.state_id, "")
        self.assertAlmostEqual(c1.name, "")


if __name__ == "__main__":
    unittest.main()