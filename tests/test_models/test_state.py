#!/usr/bin/python3
"""testing state"""
from models.state import State
from tests.test_models.test_base_model import test_basemodel


class test_state(test_basemodel):
    """ test state"""

    def __init__(self, *args, **kwargs):
        """init """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name(self):
        """testing state's name """
        new_sn = self.value()
        self.assertEqual(type(new_sn.name), str)
