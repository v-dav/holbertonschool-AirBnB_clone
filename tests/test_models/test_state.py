#!/usr/bin/python3
"""Unittest for the state module"""


import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Tests"""
    def test_default_attributes(self):
        """Tests"""
        state = State()
        self.assertEqual(state.name, "")


if __name__ == "__main__":
    unittest.main()
