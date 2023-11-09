#!/usr/bin/python3
"""
    Contains a base class that defines all common attributes/methods
    for others classes
"""
import uuid
import datetime


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
                self.key = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now().isoformat()
            self.updated_at = self.created_at

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
        self.updated_at = datetime.datetime.now().isoformat()

    def to_dict(self):
        """
            Returns a dictionary containing all keys/values of the
            __dict__ of the instance
        """
        dictionary = {}
        dictionary["id"] = self.id
        dictionary["created_at"] = self.created_at
        dictionary["updated_at"] = self.updated_at
        dictionary["__class__"] = type(self).__name__
        return dictionary
