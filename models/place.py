#!/usr/bin/python3

"""Class Placer"""

from models.base_model import BaseModel


class Place(BaseModel):
    """A class for Place.

    Attributes:
        city_id (str): city id
        user_id (str): user id
        name (str): place's name
        description (str): place description
        number_rooms (int): number of rooms
        number_bathrooms (int): the number of bathrooms
        max_guest (int): the maximum number of guests authorized
        price_by_night (int): the cost of the place by night
        latitutude (float): the latitude of the place
        longitude (float): the longitude of the place
        amenity_ids (list): the list of amenity ids
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
