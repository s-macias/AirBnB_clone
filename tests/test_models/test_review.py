#!/usr/bin/python3
"""This module tests Review class for our project """
import unittest
import pep8
from datetime import datetime
from models.state import State
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """Testing Review class
    """

    def setUp(self):
        """ sets up the initial conditions for the test"""
        self.r1 = Review()
        self.r2 = Review()
        self.r1_dict = Review()
        self.r1_save = Review()
        self.r1_main = Review()
        self.b1 = BaseModel()

    # Atributos
    def test_uuid(self):
        """ tests that every id is unique """
        self.assertIsInstance(self.r1, Review)
        self.assertTrue(hasattr(self.r1, "id"))
        self.assertNotEqual(self.r1, self.r2)
        self.assertIsInstance(self.r1.id, str)
        self.assertNotEqual(self.r1, self.b1)

    def test_Review_pep8(self):
        """ tests pep8 compliance """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/review.py'])
        self.assertEqual(result.total_errors, 0)

    def test_type_Review_attributes(self):
        """ tests Review attributes are strings  """
        class_dict = self.r1.__class__.__dict__
        self.r1.text = "Amazing!"
        self.assertIsInstance(self.r1.user_id, str)
        self.assertIsInstance(self.r1.place_id, str)
        self.assertIsInstance(self.r1.text, str)
        self.assertTrue('user_id' in class_dict)
        self.assertTrue('place_id' in class_dict)
        self.assertTrue('text' in class_dict)
