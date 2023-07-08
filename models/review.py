#!/usr/bin/python3
""" Class Review that inherits from BaseModel """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Class Review with 3 public instances """
    place_id = ""
    user_id = ""
    text = ""
