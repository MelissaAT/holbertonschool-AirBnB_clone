#!/usr/bin/python3
"""Document module"""
import json

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects
    
    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        objs_dict = {}
        for key, obj in self.__objects.items():
            objs_dict[key] = obj.to_dict()
        with open(self.__file_path, mode ='w', encoding= "utf-8") as f:
            json.dump(objs_dict, f)

    def reload(self):
              with open(FileStorage.__file_path, mode='r', encoding='utf-8') as f:
                data = json.load(f)

                from models.base_model import BaseModel
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    obj_dict = value
                    obj = BaseModel(**obj_dict)
                    FileStorage.__objects[key] = obj