#!/usr/bin/python3
""" Module for City unittests """

import unittest
from models.engine.file_storage import FileStorage
from models.city import City
from models import storage
import models
from datetime import datetime
import os
import uuid
import json


class TestCity(unittest.TestCase):
    """Class test City"""

    def test_id(self):
        """ test of id attribute """
        self.City = City()
        self.City.id = str(uuid.uuid4())
        self.assertEqual(str, type(self.City.id))

    def test_created_at(self):
        """ test of created.at attribute """
        self.City = City()
        self.City.created_at = datetime.now()
        self.assertIsNotNone(self.City.created_at)

    def test_to_dict(self):
        """ test of to_dict method """
        self.City = City()
        dic = self.City.to_dict()
        self.assertIsInstance(dic['created_at'], str)

    def test__str__(self):
        """ test of __str__ """
        self.assertEqual(str, type(City.__str__(self)))

    def test_save_check_time(self):
        """ Tests that save method updates the time """
        self.City = City()
        self.City.name = "My_City"
        self.City.save()
        self.assertNotEqual(self.City.created_at, self.City.updated_at)

    def test_save_check_file(self):
        """ Tests that save method saves contents """
        self.City = City()
        self.City.name = 'My_City'
        self.City.save()
        with open("file.json", "r", encoding='utf-8') as f:
            read_data = f.read()
            self.assertIn(self.City.name, read_data)

    def test_CityClassAttributes(self):
        """Tests for City attributes Defined"""

        self.City3 = City()
        """Tests for attributes as none"""
        self.City3.name = None
        self.City3.state_id = None
        self.assertEqual(self.City3.name, None)
        self.assertEqual(self.City3.state_id, None)


if __name__ == '__main__':
    unittest.main()
