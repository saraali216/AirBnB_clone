#!/usr/bin/python3
"""***************** This is the  base class for all models *************"""
import uuid
from datetime import datetime
import models
from models import storage


class BaseModel:
    """A base class for all hbnb models"""

    def __init__(self, *args, **kwargs):
    """ instance_constructores """
        if not kwargs:
            self.id = str(uuid4())
            self.create_atime = datetime.now()
            self.update_atime = datetime.now()
            models.storage.new(self)
        else:
            for k, w in kwargs.items():
                if k != "__class__":
                    if k == "updated_at":
                        self.update_atime = datetime.fromisoformat(w)
                    elif k == "created_at":
                        self.create_atime = datetime.fromisoformat(w)
                    else:
                        setattr(self, k, w)
    def __str__(self):
        """Returns a string represents the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates update_atime with current time when smthg changes"""
        self.updated_atime = datetime.now()
        storage.save()

    def to_dict(self):
        """Convert instance into dict"""
        dictio = {}
        dictio.update(self.__dict__)
        dictio.update({'__class__':
                (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictio['updated_atime'] = self.updated_atime.isoformat()
        dictio['created_atime'] = self.created_atime.isoformat()
        return dictio
