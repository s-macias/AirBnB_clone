#!/usr/bin/python3
"""This module tests User class for our project """
import unittest
import pep8
from datetime import datetime
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Testing User class
    """

    def setUp(self):
        """ sets up the initial conditions for the test"""
        self.u1 = User()
        self.u2 = User()
        self.user_dict = User()
        self.user_save = User()
        self.user_main = User()
        self.b1 = BaseModel()

    # Atributos
    def test_uuid(self):
        """ tests that every id is unique """
        self.assertIsInstance(self.u1, User)
        self.assertTrue(hasattr(self.u1, "id"))
        self.assertNotEqual(self.u1, self.u2)
        self.assertIsInstance(self.u1.id, str)
        self.assertNotEqual(self.u1, self.b1)

    def test_user_pep8(self):
        """ tests pep8 compliance """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/user.py'])
        self.assertEqual(result.total_errors, 0)

    def test_type_user_attributes(self):
        """ tests user attributes are strings  """
        self.u1.first_name = "John"
        self.assertIsInstance(self.u1.first_name, str)
        self.u1.last_name = "Smith"
        self.assertIsInstance(self.u1.last_name, str)
        self.u1.email = "jsmith@gmail.com"
        self.assertIsInstance(self.u1.email, str)
        self.u1.password = "$%&778Yhh"
        self.assertIsInstance(self.u1.password, str)
