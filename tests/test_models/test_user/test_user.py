#!/usr/bin/python3
""" Module for User unittests """

import unittest
from models.engine.file_storage import FileStorage
from models.user import User
from models import storage
import models
from datetime import datetime
import os
import uuid
import json


class TestUser(unittest.TestCase):
    """Class test User"""

    def test_id(self):
        """ test of id attribute """
        self.user = User()
        self.user.id = str(uuid.uuid4())
        self.assertEqual(str, type(self.user.id))

    def test_created_at(self):
        """ test of created.at attribute """
        self.user = User()
        self.user.created_at = datetime.now()
        self.assertIsNotNone(self.user.created_at)

    def test_to_dict(self):
        """ test of to_dict method """
        self.user = User()
        dic = self.user.to_dict()
        self.assertIsInstance(dic['created_at'], str)

    def test__str__(self):
        """ test of __str__ """
        self.assertEqual(str, type(User.__str__(self)))

    def test_save_check_time(self):
        """ Tests that save method updates the time """
        self.user = User()
        self.user.name = "My_User"
        self.user.save()
        self.assertNotEqual(self.user.created_at, self.user.updated_at)

    def test_save_check_file(self):
        """ Tests that save method saves contents """
        self.user = User()
        self.user.name = 'My_User'
        self.user.save()
        with open("file.json", "r", encoding='utf-8') as f:
            read_data = f.read()
            self.assertIn(self.user.name, read_data)

    def test_userClassAttributes(self):
        """Tests for user attributes Defined"""
        self.user = User()
        self.user.first_name = "Djamal"
        self.user.last_name = "Machin"
        self.user.email = "user1@email.com"
        self.user.password = "biche"

        self.assertEqual(self.user.first_name, "Djamal")
        self.assertEqual(self.user.last_name, "Machin")
        self.assertEqual(self.user.email, "user1@email.com")
        self.assertEqual(self.user.password, "biche")

        self.user2 = User()
        self.assertEqual(self.user2.first_name, "")
        self.assertEqual(self.user2.last_name, "")
        self.assertEqual(self.user2.email, "")
        self.assertEqual(self.user2.password, "")


if __name__ == '__main__':
    unittest.main()
