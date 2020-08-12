#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    name = Column(
        String(128),
        nullable=False
    )

    cities = relationship("City", backref="state", cascade="all, delete")

    @property
    def cities(self):
        """ cities getter """
        from models import storage

        all_cts = storage.all(City)
        sts_cts = []
        for city in all_cts.values():
            if self.id == city.state_id:
                sts_cts.append(city)
        return sts_cts
