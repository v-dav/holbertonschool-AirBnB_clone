#!/usr/bin/python3
""" Module for Review unittests """

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Tests"""
    def test_class(self):
        """Tests"""
        classe = Review()
        self.assertEqual(classe.place_id, "")
