#!/usr/bin/python3
"""Test cases for the Review class."""
from tests.test_models.test_base_model import BaseModelTest
from models.review import Review


class TestReview(BaseModelTest):
    """Test cases for the Review class."""

    def setUp(self):
        """Set up test environment."""
        super().setUp()
        self.cls = Review
        self.obj = self.cls()

    def test_place_id(self):
        """Test if place_id attribute is of type str."""
        self.assertIsInstance(self.obj.place_id, str)

    def test_user_id(self):
        """Test if user_id attribute is of type str."""
        self.assertIsInstance(self.obj.user_id, str)

    def test_text(self):
        """Test if text attribute is of type str."""
        self.assertIsInstance(self.obj.text, str)

