#!/usr/bin/python3
"""Module User"""
from models.base_model import BaseModel


class User(BaseModel):
    """define the user by multiple attributes"""
    first_name = ""
    mast_name = ""
    password = ""
    email = ""
