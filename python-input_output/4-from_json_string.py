#!/usr/bin/python3
"""Contains the method To JSON string to object"""


def from_json_string(my_str):
    """function that returns an object (Python data structure)
    represented by a JSON string:
    """
    import json
    return json.loads(my_str)
