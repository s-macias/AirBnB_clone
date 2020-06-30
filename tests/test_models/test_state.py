#!/usr/bin/python3
"""This module tests User class for our project """
import unittest
import pep8
from datetime import datetime
from models.state import State
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Testing User class
    """

    def setUp(self):
        """ sets up the initial conditions for the test"""
        self.s1 = State()
        self.s2 = State()
        self.s1_dict = State()
        self.state_save = State()
        self.state_main = State()
        self.b1 = BaseModel()

    # Atributos
    def test_uuid(self):
        """ tests that every id is unique """
        self.assertIsInstance(self.s1, State)
        self.assertTrue(hasattr(self.s1, "id"))
        self.assertNotEqual(self.s1, self.s2)
        self.assertIsInstance(self.s1.id, str)
        self.assertNotEqual(self.s1, self.b1)

    def test_user_pep8(self):
        """ tests pep8 compliance """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/state.py'])
        self.assertEqual(result.total_errors, 0)

    def test_type_state_attributes(self):
        """ tests State attributes are strings  """
        self.s1.name = "Florida"
        self.assertIsInstance(self.s1.name, str)
