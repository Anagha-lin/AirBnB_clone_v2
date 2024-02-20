#!/usr/bin/python3
"""Unit tests for the Amenity class."""
import unittest
from unittest.mock import patch
from models.amenity import Amenity
from models.base_model import BaseModel
from os import getenv
import pycodestyle
import inspect
import datetime
from time import sleep

storage_t = getenv("HBNB_TYPE_STORAGE")


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class."""

    def test_name_attribute(self):
        """Test the presence and type of the 'name' attribute."""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'name'))
        self.assertIsInstance(amenity.name, str)

    def test_is_subclass(self):
        """Test if Amenity is a subclass of BaseModel."""
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)

    def test_to_dict(self):
        """Test the to_dict() method."""
        amenity = Amenity()
        amenity_dict = amenity.to_dict()
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertIsInstance(amenity_dict['created_at'], str)
        self.assertIsInstance(amenity_dict['updated_at'], str)

    def test_str_method(self):
        """Test the __str__() method."""
        amenity = Amenity()
        string_output = "[Amenity] ({}) {}".format(amenity.id, amenity.__dict__)
        self.assertEqual(string_output, str(amenity))

    @patch('models.storage')
    def test_save_method(self, mock_storage):
        """Test the save() method."""
        amenity = Amenity()
        created_at = amenity.created_at
        sleep(1)
        amenity.save()
        new_created_at = amenity.created_at
        self.assertNotEqual(created_at, new_created_at)
        self.assertTrue(mock_storage.save.called)


class TestAmenityAttributes(unittest.TestCase):
    """Test cases for Amenity attributes."""

    def test_name_attribute_value(self):
        """Test the default value of 'name' attribute."""
        amenity = Amenity()
        if storage_t == 'db':
            self.assertIsNone(amenity.name)
        else:
            self.assertEqual(amenity.name, "")


class TestPEP8(unittest.TestCase):
    """Test cases to ensure PEP8 compliance."""

    def test_pep8_conformance(self):
        """Test that the code conforms to PEP8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0, "PEP8 style violations found")


if __name__ == "__main__":
    unittest.main()

