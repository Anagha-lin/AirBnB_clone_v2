#!/usr/bin/python3
"""Test cases for the User class."""
from tests.test_models.test_base_model import BaseModelTest
from models.user import User


class TestUser(BaseModelTest):
    """Test cases for the User class."""

    def setUp(self):
        """Set up test environment."""
        super().setUp()
        self.cls = User
        self.obj = self.cls()

    def test_first_name(self):
        """Test if first_name attribute is of type str."""
        self.assertIsInstance(self.obj.first_name, str)

    def test_last_name(self):
        """Test if last_name attribute is of type str."""
        self.assertIsInstance(self.obj.last_name, str)

    def test_email(self):
        """Test if email attribute is of type str."""
        self.assertIsInstance(self.obj.email, str)

    def test_password(self):
        """Test if password attribute is of type str."""
        self.assertIsInstance(self.obj.password, str)

