import unittest
from models.state import State


class TestState(unittest.TestCase):
    def test_class(self):
        classe = State()
        self.assertEqual(classe.name, "")
