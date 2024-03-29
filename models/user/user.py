#!/usr/bin/env python3
""" holds class user """


import models
from typing import Any
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from hashlib import md5
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """ Representation of a user
    """
    __tablename__ = 'users'

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    sessions = relationship('UserSession',
                            backref="users",
                            cascade="all, delete, delete-orphan")

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

    @classmethod
    def find(cls, *args, **kwargs):
        """ get a record based on the parameters passed.
        """
        if "password" in kwargs: 
            kwargs["password"] = md5(kwargs["password"].encode()).hexdigest()

        record = models.storage.get(cls, **kwargs)

        return record
