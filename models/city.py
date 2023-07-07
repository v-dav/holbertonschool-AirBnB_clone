#!/usr/bin/python3

"""Class City"""

from models.base_model import BaseModel


class City(BaseModel):
    """A City class for accomodation city.

    Attributes:
        state_id (str): the state identification
        name (str): the city's name
    """

    state_id = ""
    name = ""
