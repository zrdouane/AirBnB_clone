#!/usr/bin/python3
"""User's Module."""

from models.base_model import BaseModel


class User(BaseModel):
    """User class."""

    password = ""
    email = ""
    first_name = ""
    last_name = ""
