#!/usr/bin/python3
""" test base_model """
import unittest
import json
import os
from models.base_model import BaseModel
import datetime
from uuid import UUID


class test_basemodel(unittest.TestCase):
    """ testing base module """

    def __init__(self, *args, **kwargs):
        """init """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def delete_storage_file(self):
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_id(self):
        """test id """
        new_id = self.value()
        self.assertEqual(type(new_id.id), str)

    def setUp(self)
        """setup environement"""
        pass

    def test_default(self):
        """default testing """
        tdf = self.value()
        self.assertEqual(type(tdf), self.value)

    def test_kwargs(self):
        """test kwargs """
        tkwa = self.value()
        copy = tkwa.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is tkwa)

    def test_kwargs_int(self):
        """ testing kwargs int"""
        tkwai = self.value()
        copy = tkwai.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """ testing save """
        ts = self.value()
        ts.save()
        key = self.name + "." + ts.id
        with open('file.json', 'r') as f:
            i = json.load(f)
            self.assertEqual(i[key], ts.to_dict())

    def test_str(self):
        """ testing the str """
        tstr = self.value()
        self.assertEqual(str(tstr), '[{}] ({}) {}'.format(self.name,
                         tstr.id, tstr.__dict__))

    def test_todict(self):
        """ test to distionary """
        ttdic = self.value()
        n = ttdic.to_dict()
        self.assertEqual(ttdic.to_dict(), n)

    def test_kwargs_none(self):
        """test no kwargs ?"""
        x = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**x)

    def test_kwargs_one(self):
        """test kwargs one """
        x = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = self.value(**x)

    def test_created_attribute(self):
        """test created attribute"""
        new_att = self.value()
        self.assertEqual(type(new_att.created_attribute), datetime.datetime)

    def test_updated_attribute(self):
        """test updated attribute """
        new_att = self.value()
        self.assertEqual(type(new_att.updated_at), datetime.datetime)
        n = new_att.to_dict()
        new_att = BaseModel(**n)
        self.assertFalse(new_att.created_attribute == new_att.updated_attribute)
