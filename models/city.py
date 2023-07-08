#!/usr/bin/python3
""" Class City that inherits from BaseModel """
from models.base_model import BaseModel


class City(BaseModel):
    """ Class City with 2 public instances """
    state_id = ""
    name = ""
