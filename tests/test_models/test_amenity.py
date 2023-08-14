#!/usr/bin/python3
""" test Amenity"""
from models.amenity import Amenity
from tests.test_models.test_base_model import test_basemodel


class test_Amenity(test_basemodel):
    """ test amenity """

    def __init__(self, *args, **kwargs):
        """ init """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_scndname(self):
        """ testing second name """
        new = self.value()
        self.assertEqual(type(new.name), str)
