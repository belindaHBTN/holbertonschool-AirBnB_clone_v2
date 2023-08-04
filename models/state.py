#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    cities = relationship(
        "City", back_populates="state", cascade="all, delete, delete-orphan")

    @property
    def cities(self):
        """returns the list of City instances that belong to the state"""
        cities_dict = storage.all(City)
        temp_list = []
        for key, val in cities_dict.items():
            if self.id == val.state_id:
                temp_list[key] = val
        return temp_list
