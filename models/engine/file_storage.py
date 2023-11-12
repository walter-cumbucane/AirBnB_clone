#!/usr/bin/python3
"""
    Contains a class that serializes instances to a JSON file 
    and deserializes JSON files to instances
"""
#from models.base_model import BaseModel
import json


class FileStorage(object):
    """
        Class Definition
    """

    __file_path = "test.json"
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
        return type(self).__objects

    def new(self, obj):
        """
            Sets in the received object in the dictionary of objects
        """
        key = type(obj).__name__
        key += "."
        key += obj.id
        type(self).__objects[key] = None

    def save(self):
        """
            Serializes __objects o the JSON file specified in
            __file_path
        """
        print(type(self).__file_path)
        with open(type(self).__file_path, "w") as file:
            json_string = json.dumps(type(self).__objects)
            file.write(json_string)

    def reload(self):
        """
            Deserializes the JSON file to __objects (only if the
            JSON file exists. Otherwise, do nothing
        """
        try:
            with open(type(self).__file_path, "r") as file:
                file_data = file.read()
                type(self).__objects = json.loads(file_data)
        except Exception as e:
            pass
