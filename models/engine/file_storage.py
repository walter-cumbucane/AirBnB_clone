#!/usr/bin/python3
"""
    Contains a class that serializes instances to a JSON file
    and deserializes JSON files to instances
"""
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import json


clss = dict()
clss["BaseModel"] = BaseModel
clss["Amenity"] = Amenity
clss["City"] = City
clss["Place"] = Place
clss["Review"] = Review
clss["State"] = State
clss["User"] = User


class FileStorage(object):
    """
        Class Definition
    """

    # String - path to the JSON file
    __file_path = "file.json"

    # dictionary - empty but will store all objects
    __objects = dict()

    def __init__(self):
        """
            Class's Constructor
        """
        super().__init__()

    def all(self):
        """
            Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
            Sets in the received object in the dictionary of objects
        """
        if obj is not None:
            key = type(obj).__name__
            key += "."
            key += obj.id
            self.__objects[key] = obj

    def save(self):
        """
            Serializes __objects o the JSON file specified in
            __file_path
        """
        to_store = dict()
        for key in self.__objects:
            to_store[key] = self.__objects[key].to_dict()

        with open(self.__file_path, "w") as file:
            json_string = json.dumps(to_store)
            file.write(json_string)

    def reload(self):
        """
            Deserializes the JSON file to __objects (only if the
            JSON file exists. Otherwise, do nothing
        """
        try:
            with open(self.__file_path, "r") as file:
                file_data = file.read()
                dt = json.loads(file_data)
            for k in dt:
                self.__objects[k] = clss[dt[k]["__class__"]](**dt[k])
        except Exception as e:
            pass
