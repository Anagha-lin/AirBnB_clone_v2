#!/usr/bin/python3
"""Defines the State class."""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class State(BaseModel, Base):
    """Represents a state."""
    __tablename__ = "states"
    
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete", backref="state")

    @property
    def cities(self):
        """Gets the list of cities in the state."""
        from models import storage
        from models.city import City
        
        all_cities = storage.all(City)
        state_cities = [city for city in all_cities.values()
                        if city.state_id == self.id]
        return state_cities

