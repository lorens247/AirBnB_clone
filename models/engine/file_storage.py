#!/usr/bin/python3
"""Defines a class FileStorage that serializes instances to a JSON file
and deserializes JSON file to instances."""

import json


class FileStorage:
    """A class used to serialize and deserialize JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return type(self).__objects
    
    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        type(self).__objects[obj.__class__.__name__ + '.' + str(obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        serialized = {}
        for key, value in type(self).__objects.items():
            serialized[key] = value.to_dict()
        with open(type(self).__file_path, mode='w', encoding="UTF-8") as f:
            for key in serialized.keys():
                json.dump(serialized, f)
                f.write("\n")

    def classes(self):
        """Returns a dictionary of valid classes and their references."""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        classes = {'BaseModel': BaseModel,
                    'User': User,
                    'State': State,
                    'City': City,
                    'Amenity': Amenity,
                    'Place': Place,
                    'Review': Review}
        return classes

    def reload(self):
        """deserializes the JSON file to __objects(Only if the JSON file
        (__file_path)exists; otherwise, does nothing. if the file doesn't exist
        no exception is raised)"""
        try:
            with open(type(self).__file_path, mode='r', encoding="UTF-8") as f:
                for line in f:
                    data = json.loads(line)
                    from models.base_model import BaseModel
                    from models.user import User
                    from models.state import State
                    from models.city import City
                    from models.amenity import Amenity
                    from models.place import Place
                    from models.review import Review
                    classes = {'BaseModel': BaseModel,
                               'User': User,
                               'State': State,
                               'City': City,
                               'Amenity': Amenity,
                               'Place': Place,
                               'Review': Review}
                    for key, value in data.items():
                        class_name, obj_id = key.split('.')
                        obj = classes[class_name](**value)
                        type(self).__objects[key] = obj

        except FileNotFoundError:
            pass
