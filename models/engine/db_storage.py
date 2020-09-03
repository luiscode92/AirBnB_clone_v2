#!/usr/bin/python3
""" New engine """
from models.base_model import BaseModel, Base
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.state import State

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv


class DBStorage:
    """ class new engine """

    __engine = None
    __session = None

    def __init__(self):
        """ constructor """
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}:3306/{}'
            .format(
                getenv('HBNB_MYSQL_USER'),
                getenv('HBNB_MYSQL_PWD'),
                getenv('HBNB_MYSQL_HOST'),
                getenv('HBNB_MYSQL_DB')
            ), pool_pre_ping=True
        )
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Returns a dictionary of object """
        dict_ins = {}
        if cls is None:
            new_query = self.__session.query(
                User,
                State,
                City,
                Amenity,
                Place,
                Review
            ).all()
        else:
            new_query = self.__session.query(cls).all()

        for obj in new_query:
            key = type(obj).__name__ + "." + str(obj.id)
            dict_ins[key] = obj

        return dict_ins

    def new(self, obj):
        """ add the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ commit all changes of the current database session """
        self.__session.commit()

    def reload(self):
        """ Loads storage dictionary from file """
        Base.metadata.create_all(self.__engine)

        session_factory = sessionmaker(
            bind=self.__engine,
            expire_on_commit=False
        )
        Session = scoped_session(session_factory)
        self.__session = Session()

    def delete(self, obj=None):
        """ Deletes from the current database session """
        if obj:
            self.__session.delete(obj)

    def close(self):
        """call remove() method on the private session attribute
        """
        self.__session.close()
