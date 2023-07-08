#!/usr/bin/python3
"""
Unittest for Amenity class
"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):

    def test_create_class(self):
        a1 = Amenity()
        self.assertIsInstance(a1, Amenity)
        self.assertTrue(hasattr(a1, "name"))
        
    def test_empty_attributes(self):
        a1 = Amenity()
        self.assertAlmostEqual(a1.name, "")


if __name__ == "__main__":
    unittest.main()