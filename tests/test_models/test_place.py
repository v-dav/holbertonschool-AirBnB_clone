#!/usr/bin/python3
""" Module for Place unittests """

import unittest
from models.engine.file_storage import FileStorage
from models.place import Place
from models import storage
import models
from datetime import datetime
import os
import uuid
import json


class TestPlace(unittest.TestCase):
    """Class test Place"""

    def test_id(self):
        """ test of id attribute """
        self.Place = Place()
        self.Place.id = str(uuid.uuid4())
        self.assertEqual(str, type(self.Place.id))

    def test_created_at(self):
        """ test of created.at attribute """
        self.Place = Place()
        self.Place.created_at = datetime.now()
        self.assertIsNotNone(self.Place.created_at)

    def test_to_dict(self):
        """ test of to_dict method """
        self.Place = Place()
        dic = self.Place.to_dict()
        self.assertIsInstance(dic['created_at'], str)

    def test__str__(self):
        """ test of __str__ """
        self.assertEqual(str, type(Place.__str__(self)))

    def test_save_check_time(self):
        """ Tests that save method updates the time """
        self.Place = Place()
        self.Place.name = "My_Place"
        self.Place.save()
        self.assertNotEqual(self.Place.created_at, self.Place.updated_at)

    def test_save_check_file(self):
        """ Tests that save method saves contents """
        self.Place = Place()
        self.Place.name = 'My_Place'
        self.Place.save()
        with open("file.json", "r", encoding='utf-8') as f:
            read_data = f.read()
            self.assertIn(self.Place.name, read_data)

    def test_PlaceClassAttributes(self):
        """Tests for Place attributes Defined"""

        self.Place3 = Place()
        """Tests for attributes as none"""
        self.Place3.city_id = None
        self.Place3.user_id = None
        self.Place3.name = None
        self.Place3.description = None
        self.Place3.number_rooms = None
        self.Place3.number_bathromms = None
        self.Place3.max_guest = None
        self.Place3.price_by_night = None
        self.Place3.latitude = None
        self.Place3.longitude = None
        self.Place3.amenity_ids = None

        self.assertEqual(self.Place3.city_id, None)
        self.assertEqual(self.Place3.user_id, None)
        self.assertEqual(self.Place3.name, None)
        self.assertEqual(self.Place3.description, None)
        self.assertEqual(self.Place3.number_rooms, None)
        self.assertEqual(self.Place3.number_bathromms, None)
        self.assertEqual(self.Place3.max_guest, None)
        self.assertEqual(self.Place3.price_by_night, None)
        self.assertEqual(self.Place3.latitude, None)
        self.assertEqual(self.Place3.longitude, None)
        self.assertEqual(self.Place3.amenity_ids, None)


if __name__ == '__main__':
    unittest.main()
