#!/usr/bin/env python3
""" Storage Module
"""
import typing
from models.base_model import Base
from models.user import User
from models.user_session import UserSession
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


classes: typing.Dict = {"User": User, "UserSession": UserSession}


class DBStorage:
    """ Class DBStorage
    """
    __engine = None
    __session = None

    def __init__(self) -> None:
        """ Initialize the DBStorage.
        """
        connection_string = {
            'dev': 'mysql+mysqlconnector://sacco_test:sacco_test_pwd@localhost:3306/sacco_test_db',
            'test': 'sqlite:///db.sqlite'
        }

        self.__engine = create_engine(connection_string.get('dev'))

        # If a valid test
        Base.metadata.drop_all(self.__engine)

    def all(self, cls: typing.TypeVar = None) -> typing.Dict:
        """ Retrieve a list of records in storage
        """
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj=None):
        """ Add the object to the current database session
        """
        if obj is None:
            return

        try:
            self.__session.add(obj)
            self.__session.flush()
            self.__session.refresh(obj)
        except Exception as e:
            self.__session.rollback()
            raise e

    def save(self):
        """ Commit all changes of the current database session
        """
        self.__session.commit()

    def reload(self):
        """ Reloads data from the database
        """
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def delete(self, obj=None):
        """ Delete from the current database session obj if not None
        """
        if obj is not None:
            self.__session.delete(obj)

    def close(self):
        """ call remove() method on the private session attribute
        """
        self.__session.remove()

    def get(self, cls, **kwargs) -> typing.Any:
        """ Returns the object based on the class name and its ID, or
        None if not found
        """
        if cls not in classes.values():
            return None
        
        return self.__session.query(cls).filter_by(**kwargs).first()

        # all_cls = self.all(cls)
        # for value in all_cls.values():
        #     if (value.id == id):
        #         return value

        # return None

    def count(self, cls=None) -> int:
        """ count the number of objects in storage
        """
        all_class = classes.values()

        if not cls:
            count = 0
            for clas in all_class:
                count += len(self.all(clas).values())
        else:
            count = len(self.all(cls).values())

        return count
