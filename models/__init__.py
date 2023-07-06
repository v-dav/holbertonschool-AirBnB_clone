#!/usr/bin/python3
"""A module for unique FileStorage instance"""

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
