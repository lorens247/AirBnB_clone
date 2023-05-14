#!/use/bin/python3
"""This defines is the first user class the inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """A user class the inherits from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
