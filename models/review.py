#!/usr/bin/python3

"""Class Review"""

from models.base_model import BaseModel


class Review(BaseModel):
    """A class for Reviews.

    Attributes:
        place_id (str): the id of the place
        user_id (str): the id of the user
        text (str): the text containing the review
    """

    place_id = ""
    user_id = ""
    text = ""
