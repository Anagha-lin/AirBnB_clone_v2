#!/usr/bin/python3
"""This is the state class"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
import models
import shlex


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities_rel = relationship("City", cascade='all, delete, delete-orphan',
                              backref="state")

    @property
    def cities(self):
        """getter attribute cities that returns the list of City instances"""
        cities_dict = models.storage.all(City)
        return [city for city in cities_dict.values() if city.state_id == self.id]

