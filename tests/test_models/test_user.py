#!/usr/bin/python3
"""test user"""
from models.user import User
from tests.test_models.test_base_model import test_basemodel


class test_User(test_basemodel):
    """ test user"""

    def __init__(self, *args, **kwargs):
        """ init """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """test first name """
        new_fn = self.value()
        self.assertEqual(type(new_fn.first_name), str)

    def test_last_name(self):
        """testing last name """
        new_ln = self.value()
        self.assertEqual(type(new_ln.last_name), str)

    def test_email(self):
        """test email """
        new_email = self.value()
        self.assertEqual(type(new_email.email), str)

    def test_password(self):
        """ testing password"""
        new_pwd = self.value()
        self.assertEqual(type(new_pwd.password), str)
