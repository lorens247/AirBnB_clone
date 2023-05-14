#!/usr/bin/python3
"""Defines a class City that is the template for city object"""
from models.base_model import BaseModel


class City(BaseModel):
    """Class representing a city"""
    state_id = ""
    name = ""
