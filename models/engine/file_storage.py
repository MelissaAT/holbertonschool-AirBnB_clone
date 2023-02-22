#!/usr/bin/python3
"""Documentation Module"""

import json

from models.base_model import BaseModel


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id"""
        key_obj = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key_obj] = obj

    def save(self):
        """
        this method opens file via file_path and serialize the python
        objet in to a json one using the json.dump function
        """
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        """
        This module decerialize the json string from file
        in to a python object
         """
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                self.__objects = {k: BaseModel(**v) for k,
                                  v in json.load(f).items()}
        except Exception:
            pass
