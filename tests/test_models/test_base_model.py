#!/usr/bin/python3
"""testing on my base model"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
from models import storage


class TestBaseModel(unittest.TestCase):
    """test class for max_integer """
    my_model = BaseModel()
    my_model.name = "My First Model"
    my_model.my_number = 89

    def test_save(self):
        """"testing the save class method """
        bf_up_time = self.my_mdl.updated_at
        self.my_mdl.my_number = 90
        self.my_model.save()
        af_up_time = self.my_mdl.updated_at
        self.assertNotEqual(bfe_up_time, af_up_time)

    def test_str(self):
        """check for string representaion"""
        xstr = self.my_mdl.__class__.__name__
        expctd_str = f"[{xstr}] ({self.my_mdl.id}) <{self.my_mdl.__dict__}>"
        self.assertEqual(self.my_mdl.__str__(), expctd_str)

    def test_create_instance_without_kwargs(self):
        """creating instance of class without kwargs"""
        self.assertIsInstance(self.my_mdl, BaseModel)
        self.assertIsInstance(self.my_mdl.id, str)
        self.assertIsInstance(self.my_mdl.created_at, datetime)
        self.assertIsInstance(self.my_mdl.updated_at, datetime)
        self.assertEqual(self.my_mdl.name, "My First Model")
        self.assertEqual(self.my_mdl.my_number, 89)

    def test_create_instance_with_kwargs(self):
        """ creating instance of class with kwargs """
        my_json = self.my_mdl.to_dict()
        new_basemodel = BaseModel(**my_json)
        self.assertIsInstance(new_basemodel, BaseModel)
        self.assertIsInstance(new_basemodel.id, str)
        self.assertIsInstance(new_basemodel.created_at, datetime)
        self.assertIsInstance(new_basemodel.updated_at, datetime)
        self.assertEqual(new_basemodel.name, "My First Model")
        self.assertEqual(new_basemodel.my_number, 89)
        self.assertNotEqual(new_basemodel, self.my_mdl)
        self.assertDictEqual(new_basemodel.__dict__, self.my_mdl.__dict__)

    def test_to_dict(self):
        """ test to_dict class method """
        to_dict_rtrnd_dict = self.my_mdl.to_dict()
        expctd_dic = self.my_mdl.__dict__.copy()
        expctd_dic["__class__"] = self.my_mdl.__class__.__name__
        expctd_dic["updated_at"] = self.my_mdl.updated_at.isoformat()
        expctd_dic["created_at"] = self.my_mdl.created_at.isoformat()
        self.assertDictEqual(expctd_dic, to_dict_rtrnd_dict)
