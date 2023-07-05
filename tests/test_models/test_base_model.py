#!/usr/bin/python3
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Unittest for class BaseModel"""
    def setUp(self):
        """Set up for the tests"""
        self.my_model = BaseModel()

    def test_init(self):
        """Test for initialization"""
        self.assertTrue(isinstance(self.my_model, BaseModel))
        self.assertIsInstance(self.my_model.id, str)
        self.assertIsInstance(self.my_model.created_at, datetime)
        self.assertIsInstance(self.my_model.updated_at, datetime)
