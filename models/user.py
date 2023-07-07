#!/usr/bin/python3

"""Class User"""

from base_model import BaseModel

class User(BaseModel):
    """Class representing user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""


from engine.file_storage import FileStorage
from __init__ import storage

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new User --")
my_user = User()
my_user.first_name = "Betty"
my_user.last_name = "Bar"
print(my_user)
