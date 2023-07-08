#!/usr/bin/python3
"""
Unittest for Review class
"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):

    def test_create_class(self):
        r1 = Review()
        self.assertIsInstance(r1, Review)
        self.assertTrue(hasattr(r1, "place_id"))
        self.assertTrue(hasattr(r1, "user_id"))
        self.assertTrue(hasattr(r1, "text"))
        
    def test_empty_attributes(self):
        r1 = Review()
        self.assertAlmostEqual(r1.place_id, "")
        self.assertAlmostEqual(r1.user_id, "")
        self.assertAlmostEqual(r1.text, "")


if __name__ == "__main__":
    unittest.main()