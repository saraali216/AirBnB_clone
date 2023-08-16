#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


classes = {"BaseModel": BaseModel, "User": User, "City": City,
           "Place": Place, "Amenity": Amenity, "Review": Review,
           "State": State}


class FileStorage:
    """ This class file_storage-JSON"""

    def __init__(self):
        """string path to file JSON"""
        self.__file_path = 'file.json'
        self.__objects = {}

    def all(self):
        """returns the dictionary of __objects"""
        return self.__objects

    def save(self):
        """ serializes __objects to JSON"""
        new_dict = {}
        with open(self.__file_path, 'w', encoding="UTF-8") as filejson:
            for i, v in self.__objects.items():
                new_dict[i] = v.to_dict()
            filejson.write(json.dumps(new_dict))

    def new(self, obj):
        """sets related to the __objects"""
        mn_obj = obj.__class__.__name__ + '.' + obj.id
        self.__objects.update({mn_obj: obj})

    def reload(self):
        """ parsing the JSON file to __objects"""
        if os.path.isfile(self.__file_path):
            with open(self.__file_path) as json_f:
                other_dict_objs = json.load(json_f)
            for i, v in other_dict_objs.items():
                self.__objects[i] = eval(v["__class__"])(**v)
