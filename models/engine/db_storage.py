#!/usr/bin/python3
""" Use sqlAlchemy to declare a database storage"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os


class DBStorage():
    """database storage engine"""
    __engine = None
    __session = None

    def __init__(self):
        """Start link class to table in database"""
        username = os.getenv("HBNB_MYSQL_USER", default=None)
        password = os.getenv("HBNB_MYSQL_PWD", default=None)
        hostname = os.getenv("HBNB_MYSQL_HOST", default=None)
        database = os.getenv("HBNB_MYSQL_DB", default=None)
        env = os.getenv("HBNB_ENV", default=None)

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'\
                .format(username, password, hostname, database), pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self,cls=None):
        Session = sessionmaker(bind=engine)
        self.__session = Session(cls)
        if cls is None:
            query = self.__session.query(User, State, City, Amenity, Review).all()
        else:
            query = self.__session.query(cls).all()
        temp_dict = {}
        for obj in query:
            class_name = obj."__class__"
            obj_id = obj."id"
            key = class_name + "." + obj_id
            temp_dict[key] = obj
        return temp_dict
