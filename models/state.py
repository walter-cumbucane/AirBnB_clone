#!/usr/bin/python
"""
    This is the State module, which defines the State class.
    The State class represents new states and holds information
    about them.
"""
from models.base_model import BaseModel


class State(BaseModel):
    """state representation"""
    name = ""

    def __init__(self, *args, **kwargs):
        """state initalization"""
        super().__init__(*args, **kwargs)
