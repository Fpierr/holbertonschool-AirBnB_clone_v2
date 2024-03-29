#!/usr/bin/python3
""" State Module for HBNB project """

import os
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey
from models.city import City
from models.base_model import BaseModel
import models


class State(BaseModel):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    cities =  relationship("City", backref="state", cascade="delete")

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        @property
        def cities(self):
            """get list for ralation of the object cities"""
            city_list = []
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
