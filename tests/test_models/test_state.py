#!/usr/bin/python3
""" Module for State unittests """


import unittest
from models.engine.file_storage import FileStorage
from models.state import State
from models import storage
import models
from datetime import datetime
import os
import uuid
import json


class TestState(unittest.TestCase):
    """Class test State"""

    def test_id(self):
        """ test of id attribute """
        self.State = State()
        self.State.id = str(uuid.uuid4())
        self.assertEqual(str, type(self.State.id))

    def test_created_at(self):
        """ test of created.at attribute """
        self.State = State()
        self.State.created_at = datetime.now()
        self.assertIsNotNone(self.State.created_at)

    def test_to_dict(self):
        """ test of to_dict method """
        self.State = State()
        dic = self.State.to_dict()
        self.assertIsInstance(dic['created_at'], str)

    def test__str__(self):
        """ test of __str__ """
        self.assertEqual(str, type(State.__str__(self)))

    def test_save_check_time(self):
        """ Tests that save method updates the time """
        self.State = State()
        self.State.name = "My_State"
        self.State.save()
        self.assertNotEqual(self.State.created_at, self.State.updated_at)

    def test_save_check_file(self):
        """ Tests that save method saves contents """
        self.State = State()
        self.State.name = 'My_State'
        self.State.save()
        with open("file.json", "r", encoding='utf-8') as f:
            read_data = f.read()
            self.assertIn(self.State.name, read_data)

    def test_StateClassAttributes(self):
        """Tests for State attributes Defined"""

        self.State3 = State()
        """Tests for attributes as none"""
        self.State3.name = None

        self.assertEqual(self.State3.name, None)


if __name__ == '__main__':
    unittest.main()
