#!/usr/bin/python3
"""Unit tests for the City class."""
import unittest
import os
import pep8
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Test cases for the City class."""

    def setUp(self):
        """Set up test environment."""
        self.city = City()
        self.city.name = "LA"
        self.city.state_id = "CA"

    def tearDown(self):
        """Clean up test environment."""
        del self.city
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8(self):
        """Test PEP8 compliance."""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0, "PEP8 style errors found")

    def test_docstring(self):
        """Test for presence of docstrings."""
        self.assertIsNotNone(City.__doc__)

    def test_attributes(self):
        """Test for presence of expected attributes."""
        attributes = ['id', 'created_at', 'updated_at', 'state_id', 'name']
        for attr in attributes:
            self.assertTrue(hasattr(self.city, attr))

    def test_is_subclass(self):
        """Test if City is a subclass of BaseModel."""
        self.assertTrue(issubclass(City, BaseModel))

    def test_attribute_types(self):
        """Test for correct attribute types."""
        self.assertIsInstance(self.city.name, str)
        self.assertIsInstance(self.city.state_id, str)

    def test_save(self):
        """Test if changes are saved properly."""
        prev_updated_at = self.city.updated_at
        self.city.save()
        self.assertNotEqual(prev_updated_at, self.city.updated_at)

    def test_to_dict(self):
        """Test the to_dict() method."""
        city_dict = self.city.to_dict()
        self.assertIsInstance(city_dict, dict)
        self.assertEqual(city_dict['__class__'], 'City')


if __name__ == "__main__":
    unittest.main()

