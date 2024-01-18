#!/usr/bin/env python3
""" holds class user """


from typing import Any
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from hashlib import md5


class User(BaseModel, Base):
    """ Representation of a user
    """
    __tablename__ = 'users'

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    def __init__(self, *args, **kwargs) -> None:
        """ initializes user
        """
        super().__init__(*args, **kwargs)

    def __setattr__(self, name: str, value: Any) -> None:
        """ sets a password with md5 encryption
        """
        if name == "password":
            value = md5(value.encode()).hexdigest()
        return super().__setattr__(name, value)
