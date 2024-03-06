#!/usr/bin/env python3
""" User class module """
from base_model import BaseModel


class User(BaseModel):
    """" User class that iherits BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
