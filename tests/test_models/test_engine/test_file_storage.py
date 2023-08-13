#!/usr/bin/python3
""" Test Module for testing file storage"""
import unittest
import os
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage


class test_fileStorage(unittest.TestCase):
    """ Class to test the file storage method """

    def setUp(self):
        """ Setting up the environment for testing"""
        delete_list = []
        for key in storage._FileStorage__objects.keys():
            delete_list.append(key)
        for key in delete_list:
            del storage._FileStorage__objects[key]

    def test_object_empty_list(self):
        """ initially the __object is empty """
        self.assertEqual(len(storage.all()), 0)

    def test_new(self):
        """ New object is correctly added to __objects """
        new = BaseModel()
        for obj in storage.all().values():
            tmp = obj
        self.assertTrue(tmp is obj)

    def test_all(self):
        """ __objects is properly returned """
        tmp = storage.all()
        new = BaseModel()
        self.assertIsInstance(tmp, dict)

    def test_base_model_is_not_created(self):
        """ File is not created on BaseModel save """
        new = BaseModel()
        self.assertFalse(os.path.exists('file.json'))

    def test_empty(self):
        """ Data is saved to file """
        new = BaseModel()
        new_obj = new.to_dict()
        new.save()
        new2 = BaseModel(**new_obj)
        self.assertNotEqual(os.path.getsize('file.json'), 0)

    def test_save(self):
        """ FileStorage save method """
        new = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_base_model_save(self):
        """ BaseModel save method calls storage save """
        new = BaseModel()
        new.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_type_path(self):
        """ Confirm __file_path is a string file"""
        self.assertEqual(type(storage._FileStorage__file_path), str)

    def test_type_objects(self):
        """ Confirm that the __object is a dict """
        self.assertEqual(type(storage.all()), dict)

    def test_key_format(self):
        """ Key is properly formatted """
        new = BaseModel()
        _id = new.to_dict()['id']
        for key in storage.all().keys():
            temp = key
        self.assertEqual(temp, 'BaseModel' + '.' + _id)

    def test_storage_var_created(self):
        """ FileStorage object storage is created """
        print(type(storage))
        self.assertEqual(type(storage), FileStorage)

    def remove_Storage_file(self):
        """ Remove storage file after finishing test """
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_reload(self):
        """ Storage file is successfully loaded to __objects """
        new = BaseModel()
        storage.save()
        storage.reload()
        for x_obj in storage.all().values():
            loaded = x_obj
        self.assertEqual(new.to_dict()['id'], loaded.to_dict()['id'])

    def test_reload_empty(self):
        """ Load from an empty file """
        with open('file.json', 'w') as f:
            pass
        with self.assertRaises(ValueError):
            storage.reload()

    def test_reload_from_none_existent(self):
        """ File don't exist -> do nthg """
        self.assertEqual(storage.reload(), None)
