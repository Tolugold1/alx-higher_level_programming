#!/usr/bin/python3
"""""function that creates an Object from JSON filea 
import json


def load_from_json_file(filename):
    """Creates an Object from a JSON file"""
    with open(filename, 'r') as f:
        return json.loads(f.read())
