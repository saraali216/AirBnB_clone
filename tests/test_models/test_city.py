#!/usr/bin/python3
"""testing city """
from models.city import City
from tests.test_models.test_base_model import test_basemodel


class test_City(test_basemodel):
    """ test city"""

    def __init__(self, *args, **kwargs):
        """init """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ test state of the id"""
        new_id = self.value()
        self.assertEqual(type(new_id.state_id), str)

    def test_name(self):
        """testing names """
        new_name = self.value()
        self.assertEqual(type(new_name.name), str)
