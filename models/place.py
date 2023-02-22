#!/usr/bin/pyhton3
"""Module Class Place"""

from models.base_model import BaseModel


class Place(BaseModel):
    """Place class"""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathroom = 0
    max_guest = 0
    price_by_night = 0
    latitue = 0.0
    longitud = 0.0
    amenity_ids = []
