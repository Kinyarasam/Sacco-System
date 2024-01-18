#!/usr/bin/env python3
""" base_model module
"""
import sqlalchemy
import uuid
import datetime
import models
from sqlalchemy.ext.declarative import declarative_base

time = "%Y-%m-%dT%H:%M:%S.%f"

Base = declarative_base()


class BaseModel:
    """The BaseModel class from which future classes will be derived
    """
    id = sqlalchemy.Column(sqlalchemy.String(60), primary_key=True)
    created_at = sqlalchemy.Column(sqlalchemy.DateTime)
    updated_at = sqlalchemy.Column(sqlalchemy.DateTime)

    def __init__(self, *args, **kwargs) -> None:
        """ Initialization of the Base Model
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.datetime.strptime(
                    kwargs["created_at"], time)
            else:
                self.created_at = datetime.datetime.now(datetime.UTC)
            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.datetime.strptime(
                    kwargs["updated_at"], time)
            else:
                self.updated_at = datetime.datetime.now(datetime.UTC)
            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now(datetime.UTC)
            self.updated_at = self.created_at

    def __str__(self) -> str:
        """ String representation of the BaseModel class
        """
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        """ Updates the attribute 'updated_at' with the current datetime
        """
        self.updated_at = datetime.datetime.now(datetime.UTC)
        models.storage.new(self)
        models.storage.save()

    def to_dict(self, save_fs=None):
        """ Returns a dictionary containing all keys/values of the instance
        """
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].strftime(time)
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].strftime(time)
        new_dict["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        if save_fs is None:
            if "password" in new_dict:
                del new_dict["password"]
        return new_dict

    def delete(self):
        """ delete the current instance from the storage
        """
        models.storage.delete(self)
