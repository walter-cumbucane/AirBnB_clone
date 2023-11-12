#!/usr/bin/python3
"""
    This is the amenity class that represents new amenities.
    It defines attributes of the amenity class.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
        Amenity is a subclass of BaseModel that represents
        a new amenity. It has one attribute: * `name`:
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """Amenity initialization"""
        super().__init__(*args, **kwargs)
