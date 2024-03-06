#!/usr/bin/python3
"""This module contains TestFileStorage class"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import unittest
import os


class TestFileStorage(unittest.TestCase):
    """This class is for testing FileStorage class attributes and functions"""

    def setUp(self):
        """Setup data before each test method"""

        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """Excutes data after each test method"""

        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_new(self):
        """Tests new() function"""

        storage = FileStorage()
        self.assertEqual(storage.all(), {})

        b1 = BaseModel()

        self.assertEqual(len(storage.all()), 1)
        self.assertIn(f"BaseModel.{b1.id}", storage.all().keys())
        self.assertIn(b1, storage.all().values())

        b2 = BaseModel()

        self.assertEqual(len(storage.all()), 2)
        self.assertIn(f"BaseModel.{b2.id}", storage.all().keys())
        self.assertIn(b2, storage.all().values())

        storage.new(b2)
        self.assertEqual(len(storage.all()), 2)

        storage.new(BaseModel())
        self.assertEqual(len(storage.all()), 3)

        with self.assertRaises(TypeError):
            storage.new(BaseModel(), 4)

        with self.assertRaises(AttributeError):
            storage.new(None)

    def test_save(self):
        """Tests save() function"""

        storage = FileStorage()

        self.assertFalse(os.path.exists("file.json"))

        storage.save()

        self.assertTrue(os.path.exists("file.json"))

        with open("file.json", "r") as file1:
            file_content = file1.read()

        self.assertEqual(file_content, "{}")

        b1 = BaseModel()

        self.assertEqual(len(storage.all()), 1)

        b1.save()

        with open("file.json", "r") as file2:
            file_content = file2.read()

        self.assertIn(f"BaseModel.{b1.id}", file_content)

        b2 = BaseModel()
        storage.save()
        with open("file.json", "r") as file3:
            file_content = file3.read()
        self.assertIn(f"BaseModel.{b2.id}", file_content)

        with self.assertRaises(TypeError):
            storage.save(None)

        with self.assertRaises(TypeError):
            storage.save(BaseModel(), 10)

    def test_reload(self):
        """Tests reload() function"""

        storage = FileStorage()

        self.assertEqual(storage.all(), {})

        b1 = BaseModel()
        storage.save()
        storage.reload()

        deserialized_objects = storage.all()
        self.assertIn(f"BaseModel.{b1.id}", deserialized_objects)
        self.assertEqual(len(deserialized_objects), 1)

        with self.assertRaises(TypeError):
            storage.reload(None)

        FileStorage._FileStorage__objects = {}
        os.remove("file.json")
        storage.reload()
        self.assertEqual(storage.all(), {})

    def test_all(self):
        """Tests all() function"""

        storage = FileStorage()

        self.assertEqual(storage.all(), {})
        self.assertEqual(type(storage.all()), dict)

        b1 = BaseModel()
        self.assertEqual(len(storage.all()), 1)
        self.assertIn(f"BaseModel.{b1.id}", storage.all().keys())
        self.assertIn(b1, storage.all().values())

        self.assertTrue(storage.all() is FileStorage._FileStorage__objects)
        self.assertTrue(storage.all() == FileStorage._FileStorage__objects)
