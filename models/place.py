#!/usr/bin/python
"""
    The Place module defines the Place class,
    which holds attributes for a place.
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
        Defines Place class
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

    def __init__(self, *args, **kwargs):
        """Place Initialization"""
        super().__init__(*args, **kwargs)
