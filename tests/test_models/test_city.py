#!/usr/bin/python3
"""This module tests City class for our project """
import unittest
import pep8
from datetime import datetime
from models.state import State
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """Testing City class
    """

    def setUp(self):
        """ sets up the initial conditions for the test"""
        self.c1 = City()
        self.c2 = City()
        self.c1_dict = City()
        self.c1_save = City()
        self.c1_main = City()
        self.b1 = BaseModel()

    # Atributos
    def test_uuid(self):
        """ tests that every id is unique """
        self.assertIsInstance(self.c1, City)
        self.assertTrue(hasattr(self.c1, "id"))
        self.assertNotEqual(self.c1, self.c2)
        self.assertIsInstance(self.c1.id, str)
        self.assertNotEqual(self.c1, self.b1)

    def test_City_pep8(self):
        """ tests pep8 compliance """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/city.py'])
        self.assertEqual(result.total_errors, 0)

    def test_type_City_attributes(self):
        """ tests City attributes are strings  """
        class_dict = self.c1.__class__.__dict__
        self.c1.name = "parking"
        self.assertIsInstance(self.c1.name, str)
        self.assertIsInstance(self.c1.state_id, str)
        self.assertTrue('state_id' in class_dict)
