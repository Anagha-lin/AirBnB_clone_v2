#!/usr/bin/python3
"""Test cases for the Place class."""
from tests.test_models.test_base_model import BaseModelTest
from models.place import Place


class TestPlace(BaseModelTest):
    """Test cases for the Place class."""

    def setUp(self):
        """Set up test environment."""
        super().setUp()
        self.cls = Place
        self.obj = self.cls()

    def test_city_id(self):
        """Test if city_id attribute is of type str."""
        self.assertIsInstance(self.obj.city_id, str)

    def test_user_id(self):
        """Test if user_id attribute is of type str."""
        self.assertIsInstance(self.obj.user_id, str)

    def test_name(self):
        """Test if name attribute is of type str."""
        self.assertIsInstance(self.obj.name, str)

    def test_description(self):
        """Test if description attribute is of type str."""
        self.assertIsInstance(self.obj.description, str)

    def test_number_rooms(self):
        """Test if number_rooms attribute is of type int."""
        self.assertIsInstance(self.obj.number_rooms, int)

    def test_number_bathrooms(self):
        """Test if number_bathrooms attribute is of type int."""
        self.assertIsInstance(self.obj.number_bathrooms, int)

    def test_max_guest(self):
        """Test if max_guest attribute is of type int."""
        self.assertIsInstance(self.obj.max_guest, int)

    def test_price_by_night(self):
        """Test if price_by_night attribute is of type int."""
        self.assertIsInstance(self.obj.price_by_night, int)

    def test_latitude(self):
        """Test if latitude attribute is of type float."""
        self.assertIsInstance(self.obj.latitude, float)

    def test_longitude(self):
        """Test if longitude attribute is of type float."""
        self.assertIsInstance(self.obj.longitude, float)

    def test_amenity_ids(self):
        """Test if amenity_ids attribute is of type list."""
        self.assertIsInstance(self.obj.amenity_ids, list)

