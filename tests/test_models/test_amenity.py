#!/usr/bin/python3
""" Module for Amenity unittests """

import unittest
from models.engine.file_storage import FileStorage
from models.amenity import Amenity
from models import storage
import models
from datetime import datetime
import os
import uuid
import json


class TestAmenity(unittest.TestCase):
    """Class test Amenity"""

    def test_id(self):
        """ test of id attribute """
        self.Amenity = Amenity()
        self.Amenity.id = str(uuid.uuid4())
        self.assertEqual(str, type(self.Amenity.id))

    def test_created_at(self):
        """ test of created.at attribute """
        self.Amenity = Amenity()
        self.Amenity.created_at = datetime.now()
        self.assertIsNotNone(self.Amenity.created_at)

    def test_to_dict(self):
        """ test of to_dict method """
        self.Amenity = Amenity()
        dic = self.Amenity.to_dict()
        self.assertIsInstance(dic['created_at'], str)

    def test__str__(self):
        """ test of __str__ """
        self.assertEqual(str, type(Amenity.__str__(self)))

    def test_save_check_time(self):
        """ Tests that save method updates the time """
        self.Amenity = Amenity()
        self.Amenity.name = "My_Amenity"
        self.Amenity.save()
        self.assertNotEqual(self.Amenity.created_at, self.Amenity.updated_at)

    def test_save_check_file(self):
        """ Tests that save method saves contents """
        self.Amenity = Amenity()
        self.Amenity.name = 'My_Amenity'
        self.Amenity.save()
        with open("file.json", "r", encoding='utf-8') as f:
            read_data = f.read()
            self.assertIn(self.Amenity.name, read_data)

    def test_AmenityClassAttributes(self):
        """Tests for Amenity attributes Defined"""
        self.Amenity = Amenity()
        self.Amenity.name = "Amenity"

        self.assertEqual(self.Amenity.name, "Amenity")

        self.Amenity2 = Amenity()
        """Tests for attrinbutes not defined"""
        self.assertEqual(self.Amenity2.name, "")

        self.Amenity3 = Amenity()
        """Tests for attributes as none"""
        self.Amenity3.name = None
        self.assertEqual(self.Amenity3.name, None)


if __name__ == '__main__':
    unittest.main()
