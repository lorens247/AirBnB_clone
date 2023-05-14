#!/usr/bin/python3
"""defines a class that inherits from BaseModel and 
handles the states the apartments are located"""

from models.base_model import BaseModel


class State(BaseModel):
    """a class that represents a state"""
    name = ""
