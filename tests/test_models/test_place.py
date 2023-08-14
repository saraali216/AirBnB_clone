#!/usr/bin/python3
""" testing the place"""
from models.place import Place
from tests.test_models.test_base_model import test_basemodel


class test_Place(test_basemodel):
    """ test place """

    def __init__(self, *args, **kwargs):
        """ init """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """testing city id """
        new_cid = self.value()
        self.assertEqual(type(new_cid.city_id), str)

    def test_user_id(self):
        """ test user id"""
        new_uid = self.value()
        self.assertEqual(type(new_uid.user_id), str)

    def test_name(self):
        """test name """
        new_name = self.value()
        self.assertEqual(type(new_name.name), str)

    def test_description(self):
        """test description """
        new_desc = self.value()
        self.assertEqual(type(new_desc.description), str)

    def test_number_rooms(self):
        """test rooms number """
        new_rnum = self.value()
        self.assertEqual(type(new_rnum.number_rooms), int)

    def test_number_bathrooms(self):
        """ test bathroom number"""
        new_bnum = self.value()
        self.assertEqual(type(new_bnum.number_bathrooms), int)

    def test_max_guest(self):
        """test max guest """
        new_mg = self.value()
        self.assertEqual(type(new_mg.max_guest), int)

    def test_price_by_night(self):
        """test nightly price """
        new_pn = self.value()
        self.assertEqual(type(new_pn.price_by_night), int)

    def test_latitude(self):
        """test lattitude """
        new_latt = self.value()
        self.assertEqual(type(new_latt.latitude), float)

    def test_longitude(self):
        """test longitude """
        new_ltt = self.value()
        self.assertEqual(type(new_ltt.latitude), float)

    def test_amenity_ids(self):
        """test amenity ids """
        new_aid = self.value()
        self.assertEqual(type(new_aid.amenity_ids), list)
