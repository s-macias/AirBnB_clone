#!/usr/bin/python3
"""This module tests Amenity class for our project """
import unittest
import pep8
from datetime import datetime
from models.state import State
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Testing Amenity class
    """

    def setUp(self):
        """ sets up the initial conditions for the test"""
        self.a1 = Amenity()
        self.a2 = Amenity()
        self.a1_dict = Amenity()
        self.a1_save = Amenity()
        self.a1_main = Amenity()
        self.b1 = BaseModel()

    # Atributos
    def test_uuid(self):
        """ tests that every id is unique """
        self.assertIsInstance(self.a1, Amenity)
        self.assertTrue(hasattr(self.a1, "id"))
        self.assertNotEqual(self.a1, self.a2)
        self.assertIsInstance(self.a1.id, str)
        self.assertNotEqual(self.a1, self.b1)

    def test_amenity_pep8(self):
        """ tests pep8 compliance """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/amenity.py'])
        self.assertEqual(result.total_errors, 0)

    def test_type_amenity_attributes(self):
        """ tests Amenity attributes are strings  """
        self.a1.name = "parking"
        self.assertIsInstance(self.a1.name, str)
