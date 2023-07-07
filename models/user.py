#!/usr/bin/python3

"""Class User"""

from models.base_model import BaseModel


class User(BaseModel):
    """Class representing User.

    Attributes:
        email (str): user email
        password (str): user password
        first_name (str): user's first name
        last_name (str): user's last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
