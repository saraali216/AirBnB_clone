#!/usr/bin/python3
"""testing review """
from models.review import Review
from tests.test_models.test_base_model import test_basemodel


class test_review(test_basemodel):
    """test review"""

    def __init__(self, *args, **kwargs):
        """init """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_user_id(self):
        """testing user id """
        new_user_id = self.value()
        self.assertEqual(type(new_user_id.user_id), str)

    def test_place_id(self):
        """test place's id """
        new_pid = self.value()
        self.assertEqual(type(new_pid.place_id), str)

    def test_text(self):
        """ test text"""
        new_tt = self.value()
        self.assertEqual(type(new_tt.text), str)
