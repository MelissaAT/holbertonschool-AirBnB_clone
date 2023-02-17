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
        obj_c
