#!/usr/bin/python3
""" State Module for HBNB project """

import os
from models.base_model import Base
from sqlalchemy.orm import relationship
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey
from models.city import City

if os.getenv("HBNB_TYPE_STORAGE") != "db":
    from models import storage


class State(BaseModel):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", back_populates="state",
                              cascade="all, delete-orphan")
