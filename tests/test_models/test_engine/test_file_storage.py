#!/usr/bin/python3
import unittest
import pep8
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """ tests FileStorage  """
    def setUp(self):
        self.base1 = BaseModel()
        self.storage_test = FileStorage()

    def test_instantiation(self):
        """ tests correct instantiation of FileStorage class  """
        self.assertEqual(type(models.storage).__name__, "FileStorage")

    def test_noarguments(self):
        """ tests initialization without arguments  """
        with self.assertRaises(TypeError) as error:
            FileStorage.__init__()
            fail = "descriptor '__init__' of 'object' object needs an argument"
            self.assertEqual(str(error.exception), fail)

    def test_arguments(self):
        """ tests __init__ with many arguments"""
        with self.assertRaises(TypeError) as error:
            base = FileStorage(67, 7, 12, 9, 4, 5)
        fail = "object() takes no parameters"
        self.assertEqual(str(error.exception), fail)

    def test_attributes(self):
        """ tests class attributes"""
        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))
        self.assertTrue(hasattr(FileStorage, "_FileStorage__objects"))
        self.assertIsInstance(models.storage._FileStorage__objects, dict)
        self.assertIsInstance(models.storage._FileStorage__file_path, str)

    def test_docstrings(self):
        """ Checks the documentation """
        # self.assertIsNotNone(FileStorage.__doc__)
        # self.assertIsNotNone(FileStorage.__init__.__doc__)
        # self.assertIsNotNone(FileStorage.all.__doc__)
        # self.assertIsNotNone(FileStorage.new.__doc__)
        # self.assertIsNotNone(FileStorage.save.__doc__)
        # self.assertIsNotNone(FileStorage.reload.__doc__)

    def test_field_storage_exist(self):
        """ Checks if methods exists """
        self.assertTrue(hasattr(self.storage_test, "__init__"))
        self.assertTrue(hasattr(self.storage_test, "all"))
        self.assertTrue(hasattr(self.storage_test, "new"))
        self.assertTrue(hasattr(self.storage_test, "save"))
        self.assertTrue(hasattr(self.storage_test, "reload"))

    def test_saveStorage(self):
        """ Checks if the save function works """
        self.base1.name = "Halo"
        self.base1.save()  # actualiza el file.json
        models.storage.reload()  # reinicia
        models.storage.all()  # retorna __objects
        self.assertIsInstance(models.storage.all(), dict)
        self.assertTrue(hasattr(self.base1, 'save'))
        self.assertNotEqual(self.base1.created_at, self.base1.updated_at)

    def test_filestorage_pep8(self):
        """ tests pep8 compliance """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0)
