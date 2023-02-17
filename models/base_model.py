#!/usr/bin/python3
"""Documentation Module"""
import uuid
from datetime import datetime

class BaseModel:
    """Class that defines all common 
    attributes/methods for other classes"""
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.update_at = self.created_at
    def __str__(self):
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.update_at = datetime.now

    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        self.__dict__['created_at'] = (datetime.isoformat(
                                    self.__dict__.get('created_at')))
        self.__dict__['updated_at']