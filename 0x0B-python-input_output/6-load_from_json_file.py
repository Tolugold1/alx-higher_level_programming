#!/usr/bin/python3
"""""function that creates an Object from JSON filea 
import json


def load_from_json_file(filename):
    """creates an object"""
    with open(filename, 'r') as f:
        return json.loads(f.read())
