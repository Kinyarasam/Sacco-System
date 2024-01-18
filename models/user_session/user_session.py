#!/usr/bin/env python3
""" holds class UserSession """


import sqlalchemy
from models.base_model import BaseModel, Base


class UserSession(BaseModel, Base):
    """ Representation of a user_session
    """
    __tablename__ = 'user_sessions'

    user_id = sqlalchemy.Column(sqlalchemy.String(
        60), sqlalchemy.ForeignKey('users.id'), nullable=False)
    session_id = sqlalchemy.Column(sqlalchemy.String(
        60), sqlalchemy.ForeignKey('users.id'), nullable=False)
    duration = sqlalchemy.Column(sqlalchemy.String(60))
    reset_token = sqlalchemy.Column(sqlalchemy.String(60))
