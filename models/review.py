#!/usr/bin/env python3
""" Module that includes couple of classes """
from base_model import BaseModel


class Review(BaseModel):
    """Review class"""

    place_id = ""
    user_id = ""
    text = ""
