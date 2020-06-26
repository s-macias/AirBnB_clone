#!/usr/bin/python3
"""This module tests base class for our project"""
import unittest
import pep8
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Testing BaseModel class
    """

    def setUp(self):
        # print("setupppppp")
        self.b1 = BaseModel()
        self.b2 = BaseModel()
        self.basedict = BaseModel()
        self.bsave = BaseModel()
        self.bmain = BaseModel()

    # Atributos
    def test_uuid(self):
        self.assertIsInstance(self.b1, BaseModel)
        self.assertTrue(hasattr(self.b1, "id"))
        self.assertNotEqual(self.b1, self.b2)
        self.assertIsInstance(self.b1.id, str)

    def test_created(self):
        self.assertIsInstance(self.b2, BaseModel)
        self.assertTrue(hasattr(self.b2, "created_at"))
        self.assertTrue(hasattr(self.b2, "updated_at"))
        self.assertIsInstance(self.b2.created_at, datetime)
        self.assertIsInstance(self.b2.updated_at, datetime)
        self.assertNotEqual(self.b2.created_at, self.b2.updated_at)

    # Métodos
    def test_todict(self):
        # print(self.basedict.to_dict())
        self.assertTrue(type(self.basedict.to_dict()) is dict)
        dictionary = self.basedict.to_dict()
        self.assertIsInstance(dictionary['created_at'], str)
        self.assertIsInstance(dictionary['updated_at'], str)
        self.assertIsInstance(dictionary['__class__'], str)
        self.assertIsInstance(dictionary['id'], str)

    def test_save(self):
        olddate = self.bsave.updated_at
        self.bsave.save()  # update
        self.assertNotEqual(olddate, self.bsave.updated_at)
        self.assertIsInstance(self.bsave.updated_at, datetime)

    def test_str(self):
        self.assertIsInstance(self.b1.__str__(), str)

    def test_main(self):
        dictionary1 = self.bmain.to_dict()
        self.bmain.name = "Holberton"
        self.bmain.my_number = 89
        dictionary2 = self.bmain.to_dict()
        self.assertNotEqual(len(dictionary1), len(dictionary2))

    def test_basemodel_pep8(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/base_model.py'])
        self.assertEqual(result.total_errors, 0)
