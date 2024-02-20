#!/usr/bin/python3
"""Test cases for the State class."""
from tests.test_models.test_base_model import BaseModelTest
from models.state import State


class TestState(BaseModelTest):
    """Test cases for the State class."""

    def setUp(self):
        """Set up test environment."""
        super().setUp()
        self.cls = State
        self.obj = self.cls()

    def test_name(self):
        """Test if name attribute is of type str."""
        self.assertIsInstance(self.obj.name, str)

