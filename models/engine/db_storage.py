#!/usr/bin/python3
"""New engine DBStorage"""

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base


class DBStorage:
    """DBStorage class"""

    __engine = None
    __session = None

    def __init__(self):
        """Initialize DBStorage"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session"""
        from models import base_model
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.user import User
        from models.state import State
        objects = {}
        if cls:
            query = self.__session.query(cls).all()
        else:
            classes = [base_model.State, base_model.City,
                       base_model.User, base_model.Place,
                       base_model.Amenity, base_model.Review]
            query = []
            for cls in classes:
                query += self.__session.query(cls).all()
        for obj in query:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            objects[key] = obj
        return objects

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    storage = DBStorage()
