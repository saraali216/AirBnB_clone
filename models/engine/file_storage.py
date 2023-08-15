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


class FileStorage:
    """This class manages storage in JSON"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns all objects in BaseModel class"""
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves the storage dictionary into file"""
        from models import BaseModel
        with open(FileStorage.__file_path, 'w') as f:
            tmp = {}
            tmp.update(FileStorage.__objects)
            for i, j in tmp.items():
                tmp[i] = j.to_dict()
            json.dump(tmp, f)

    def reload(self):
        """Deserializes the JSON objects in file.json"""
        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            tmp = {}
            with open(FileStorage.__file_path, 'r') as f:
                tmp = json.load(f)
                for i, j in tmp.items():
                    self.all()[i] = classes[j['__class__']](**j)
        except FileNotFoundError:
            pass
        except Exception as e:
            pass
