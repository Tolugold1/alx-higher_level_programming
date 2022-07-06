#!/usr/bin/python3
"""class Student"""


class Student:
    def __init__(self, first_name, last_name, age):
        """Initialize class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student"""
        if attrs is None:
            return self.__dict__
        my_attrs = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                my_attrs[key] = value
        return my_attrs

    def reload_from_json(self, json):
        """Replace attributes of the Student instance."""
        for key, value in json.items():
            setattr(self, key, value)
