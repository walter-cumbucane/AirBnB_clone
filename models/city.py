#!/usr/bin/python
"""
The City module defines the City class, which represents a city.
"""

from models.base_model import BaseModel


class City(BaseModel):
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """City initialization"""
        super().__init__(*args, **kwargs)
