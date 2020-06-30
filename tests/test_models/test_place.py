#!/usr/bin/python3
"""This module tests Place class for our project """
import unittest
import pep8
from datetime import datetime
from models.state import State
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """Testing Place class
    """

    def setUp(self):
        """ sets up the initial conditions for the test"""
        self.p1 = Place()
        self.p2 = Place()
        self.p1_dict = Place()
        self.p1_save = Place()
        self.p1_main = Place()
        self.b1 = BaseModel()

    # Atributos
    def test_uuid(self):
        """ tests that every id is unique """
        self.assertIsInstance(self.p1, Place)
        self.assertTrue(hasattr(self.p1, "id"))
        self.assertNotEqual(self.p1, self.p2)
        self.assertIsInstance(self.p1.id, str)
        self.assertNotEqual(self.p1, self.b1)

    def test_Place_pep8(self):
        """ tests pep8 compliance """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/place.py'])
        self.assertEqual(result.total_errors, 0)

    def test_type_Place_attributes(self):
        """ tests Place attributes are strings  """
        class_dict = self.p1.__class__.__dict__
        self.p1.name = "Beautiful Flat"
        self.p1.description = "Beautiful flat located downtown."
        self.p1.max_guest = 6
        self.p1.amenity_ids = ["f456d"]
        self.assertIsInstance(self.p1.city_id, str)
        self.assertIsInstance(self.p1.user_id, str)
        self.assertIsInstance(self.p1.description, str)
        self.assertIsInstance(self.p1.number_rooms, int)
        self.assertIsInstance(self.p1.number_bathrooms, int)
        self.assertIsInstance(self.p1.max_guest, int)
        self.assertIsInstance(self.p1.price_by_night, int)
        self.assertIsInstance(self.p1.latitude, float)
        self.assertIsInstance(self.p1.longitude, float)
        self.assertIsInstance(self.p1.amenity_ids, list)
        self.assertTrue('city_id' in class_dict)
        self.assertTrue('user_id' in class_dict)
        self.assertTrue('name' in class_dict)
        self.assertTrue('description' in class_dict)
        self.assertTrue('number_rooms' in class_dict)
        self.assertTrue('number_bathrooms' in class_dict)
        self.assertTrue('max_guest' in class_dict)
        self.assertTrue('price_by_night' in class_dict)
        self.assertTrue('latitude' in class_dict)
        self.assertTrue('longitude' in class_dict)
        self.assertTrue('amenity_ids' in class_dict)
