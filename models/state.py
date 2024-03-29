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

        def __init__(self, *args, **kwargs):
            """initializes state"""
            super().__init__(*args, **kwargs)

    else:
        @property
        def cities(self):
            """Getter attribute for cities related to this state"""
            from models import storage
            from models.city import City
            city_list = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
