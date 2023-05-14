#!/usr/bin/python3
"""defines Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """handles customer review"""
    place_id = ""
    user_id  = ""
    text = ""
