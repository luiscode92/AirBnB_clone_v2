#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String,  Integer
from sqlalchemy import Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv


place_amenity = Table(
    'place_amenity',
    Base.metadata,
    Column(
        'place_id',
        String(60),
        ForeignKey('places.id'),
        primary_key=True,
        nullable=False),
    Column(
        'amenity_id',
        String(60),
        ForeignKey('amenities.id'),
        primary_key=True,
        nullable=False)
)


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship('Review', backref='place',
                               cascade='all, delete-orphan')

        amenities = relationship(
            'Amenity', secondary=place_amenity,
            viewonly=False)

    else:
        @property
        def reviews(self):
            """
            Getter that return list of Review instances
            """
            list_reviews = []
            for review in self.reviews:
                if self.id == review.place_id:
                    list_reviews.append(review)
            return list_reviews

        @property
        def amenities(self):
            """
            getter amenity that returns the list of Amenity
            """
            new_list = []
            for obj in amenity_ids:
                if obj.id == self.id:
                    new_list.append(obj)

            return new_list

        @amenities.setter
        def amenities(self, obj):
            """ Adds an Amenity.id to the attribute amenity_ids """
            if type(obj).__name__ == 'Amenity':
                self.amenity_ids.append(obj)
