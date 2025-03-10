#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'

    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        places = relationship("Place", back_populates="city",
                              cascade="all, delete, delete-orphan")

        state = relationship("State", back_populates="cities")
