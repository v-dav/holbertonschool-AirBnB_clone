#!/usr/bin/python3
""" Module for Review unittests """

import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Tests"""
    def test_class(self):
        """Tests"""
        classe = Place()
        self.assertEqual(classe.name, "")
