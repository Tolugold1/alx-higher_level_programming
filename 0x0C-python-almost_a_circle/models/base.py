#!/usr/bin/python3
"""Class Base"""
import json
from os import path


class Base:
    """define cls Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializer"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if not list_dictionaries or list_dictionaries is None:
            return '[]'
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if not json_string or json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + '.json'
        dictionary = []
        if list_objs is None:
            dictionary = [i.to_dictionary() for i in list_objs]
        with open(filename, 'w') as file:
            file.write(cls.to_json_string(dictionary))

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set."""
        if cls.__name__ == 'Rectangle':
            new_base = cls(1, 1)
        else:
            new_base = cls(1)
        cls.update(new_base, **dictionary)
        return new_base

    @classmethod
    def load_from_file(cls):
        """Return a list of instances."""
        filename = cls.__name__ + '.json'
        if path.isfile(filename):
            with open(filename, 'r') as f:
                my_list = cls.from_json_string(f.read())
            return [cls.create(**obj) for obj in my_list]
        return []
