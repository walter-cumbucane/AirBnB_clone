#!/usr/bin/python3
"""
    Contains a base class that defines all common attributes/methods
    for others classes
"""
import models
import uuid
from datetime import datetime as dt

time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel(object):
    """
        Contains the base class of the project
    """

    def __init__(self, *args, **kwargs):
        """
            Class's Constructor
        """
        if kwargs:
            for key in kwargs.keys():
                if key == "__class__":
                    continue
                setattr(self, key, kwargs[key])
            if hasattr(self, "created_at") and type(self.created_at) is str:
                self.created_at = dt.strptime(kwargs["created_at"], time)
            if hasattr(self, "updated_at") and type(self.updated_at) is str:
                self.updated_at = dt.strptime(kwargs["updated_at"], time)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = dt.now()
            self.updated_at = self.created_at
            models.storage.new(self)
            models.storage.save()

    def __str__(self):
        """
            Creates a printable object
        """
        printable = f"[{type(self).__name__}] ({self.id}) "
        printable += f"{self.__dict__}"
        return printable

    def save(self):
        """
            Updates the updated_at with the current time
        """
        self.updated_at = dt.now()
        models.storage.save()

    def to_dict(self):
        """
            Returns a dictionary containing all keys/values of the
            __dict__ of the instance
        """
        dictionary = self.__dict__.copy()
        dictionary["created_at"] = self.created_at.strftime(time)
        dictionary["updated_at"] = self.updated_at.strftime(time)
        dictionary["__class__"] = type(self).__name__
        return dictionary
