#!/usr/bin/python3
""" Module for Review unittests """

import unittest
from models.engine.file_storage import FileStorage
from models.review import Review
from models import storage
import models
from datetime import datetime
import os
import uuid
import json


class TestReview(unittest.TestCase):
    """Class test Review"""

    def test_id(self):
        """ test of id attribute """
        self.Review = Review()
        self.Review.id = str(uuid.uuid4())
        self.assertEqual(str, type(self.Review.id))

    def test_created_at(self):
        """ test of created.at attribute """
        self.Review = Review()
        self.Review.created_at = datetime.now()
        self.assertIsNotNone(self.Review.created_at)

    def test_to_dict(self):
        """ test of to_dict method """
        self.Review = Review()
        dic = self.Review.to_dict()
        self.assertIsInstance(dic['created_at'], str)

    def test__str__(self):
        """ test of __str__ """
        self.assertEqual(str, type(Review.__str__(self)))

    def test_save_check_time(self):
        """ Tests that save method updates the time """
        self.Review = Review()
        self.Review.name = "My_Review"
        self.Review.save()
        self.assertNotEqual(self.Review.created_at, self.Review.updated_at)

    def test_save_check_file(self):
        """ Tests that save method saves contents """
        self.Review = Review()
        self.Review.name = 'My_Review'
        self.Review.save()
        with open("file.json", "r", encoding='utf-8') as f:
            read_data = f.read()
            self.assertIn(self.Review.name, read_data)

    def test_ReviewClassAttributes(self):
        """Tests for Review attributes Defined"""

        self.Review3 = Review()
        """Tests for attributes as none"""
        self.Review3.place_id = None
        self.Review3.user_id = None
        self.Review3.text = None

        self.assertEqual(self.Review3.place_id, None)
        self.assertEqual(self.Review3.user_id, None)
        self.assertEqual(self.Review3.text, None)


if __name__ == '__main__':
    unittest.main()
