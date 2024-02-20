#!/usr/bin/python3
"""Defines the Amenity class."""

from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Table, ForeignKey

class Amenity(BaseModel, Base):
    """Represents an amenity in the system."""
    __tablename__ = "amenities"
    
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary=Table("place_amenity", Base.metadata,
                                                           Column("place_id", String(60), ForeignKey("places.id"), primary_key=True, nullable=False),
                                                           Column("amenity_id", String(60), ForeignKey("amenities.id"), primary_key=True, nullable=False)))

