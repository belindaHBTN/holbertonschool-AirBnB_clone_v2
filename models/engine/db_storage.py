#!/usr/bin/python3
""" Use sqlAlchemy to declare a database storage"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os


class DBStorage():
    """database storage engine"""
    __engine = None
    __session = None

    def__init__(self):
        """Start link class to table in database"""
        os.environ["HBNB_MYSQL_USER"] = hbnb_dev
        os.environ["HBNB_MYSQL_PWD"] = hbnb_dev_pwd
        os.environ["HBNB_MYSQL_HOST"] = localhost
        os.environ["HBNB_MYSQL_DB"] = hbnb_dev_db
        os.environ["HBNB_ENV"] = dev

        username = os.environ.get("HBNB_MYSQL_USER")
        password = os.environ.get("HBNB_MYSQL_PWD")
        hostname = os.environ.get("HBNB_MYSQL_HOST")
        database = os.environ.get("HBNB_MYSQL_DB")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'\
                .format(username, password, hostname, database), pool_pre_ping=True)
        #        Base.metadata.create_all(engine)

    def all(self,cls=None):
        Session = sessionmaker(bind=engine)
        self.__session = Session(cls)
        if cls is None:
            classes = []
        
        else:
            for instance in session.query(State).order_by(State.id):
                return 
