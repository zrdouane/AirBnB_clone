#!/usr/bin/python3
"""Storage Module."""
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Handle serialization and deserialization."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id."""
        key = obj.__class__.__name__ + "." + str(obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file."""
        json_obj = {}
        for key in self.__objects:
            json_obj[key] = self.__objects[key].to_dict()

        with open(self.__file_path, "w") as file:
            json.dump(json_obj, file)

    def reload(self):
        """Deserialize the JSON file to __objects."""
        try:
            """if the JSON file (__file_path) exists"""
            with open(self.__file_path, "r", encoding="UTF8") as file:
                data = json.load(file)
                for key, value in data.items():
                    attr_value = eval(value["__class__"])(**value)
                    self.__objects[key] = attr_value
        except FileNotFoundError:
            pass
