#!/usr/bin/python3
"""
function that returns an object (Python data structure) represented by a JSON string
"""


def from_json_string(my_str):
    """returns an object"""
    import json
    return json.loads(my_str)
