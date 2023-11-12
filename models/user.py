#!/usr/bin/python
"""
    This is the User module, which defines the User class.
    The User class represents new users and holds information about them.
"""

from models.base_model import BaseModel


class User(BaseModel):
    """User representation"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """User initialization"""
        super().__init__(*args, **kwargs)
