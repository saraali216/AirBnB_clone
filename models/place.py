#!/usr/bin/python3
"""Module Place """
from models.base_model import BaseModel


class Place(BaseModel):
    """A place or house in the app """
    name = ""
    city_id = ""
    user_id = ""
    amenity_ids = []
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    price_by_night = 0
    max_guest = 0
    latitude = 0.0
    longitude = 0.0
