#!/usr/bin/python3
"""***************** This is the  base class for all models *************"""
import uuid
from models.base_model import BaseModel
from base_model import BaseModel
from datetime import datetime
import models
from models import storage


class BaseModel:
    """A base Model class for hbnb models"""

    def __init__(self, *args, **kwargs):
        if kwargs:
            for x, v in kwargs.items():
                if x != "__class__":
                    if x == "created_attrbt" or x == "updated_attrbt":
                        v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, x, v)
        else:
            self.id = str(uuid4())
            self.created_attrbt = datetime.now()
            self.updated_attrbt = self.created_attrbt
            models.storage.new(self)

    def save(self):
        """updates the instance attribute -> current datatime"""
        self.updated_attrbt = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns the dictionary """
        newb = self.__dict__.copy()
        newb["__class__"] = self.__class__.__name__
        newb["updated_attrbt"] = self.updated_attrbt.isoformat()
        newb["created_attrbt"] = self.created_attrbt.isoformat()
        return newb

    def __str__(self):
        """prints the class"""
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))
