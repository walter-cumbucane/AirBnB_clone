#!/usr/bin/python
"""
    This is the Review module, which defines the Review class.
    The Review class represents new reviews and holds information
    about them.
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
        Defines the review class
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Review Initialization"""
        super().__init__(*args, **kwargs)
