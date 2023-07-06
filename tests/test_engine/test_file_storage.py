import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.file_storage = FileStorage()
        self.base_model = BaseModel()

    def test_all(self):
        initial_objects = self.file_storage.all()
        self.base_model.save()
        after_save_objects = self.file_storage.all()
        self.assertEqual(len(initial_objects), len(after_save_objects))

    def test_new(self):
        initial_objects = self.file_storage.all()
        self.file_storage.new(self.base_model)
        after_new_objects = self.file_storage.all()
        self.assertEqual(len(initial_objects), len(after_new_objects))

    def test_save(self):
        initial_objects = self.file_storage.all()
        self.file_storage.save()
        after_save_objects = self.file_storage.all()
        self.assertEqual(len(initial_objects), len(after_save_objects))

    def test_reload(self):
        initial_objects = self.file_storage.all()
        self.file_storage.reload()
        after_reload_objects = self.file_storage.all()
        self.assertEqual(len(initial_objects), len(after_reload_objects))


if __name__ == '__main__':
    unittest.main()
