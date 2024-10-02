#!/usr/bin/env python3
"""from task_00_basic_serialization import load_and_deserialize,
serialize_and_save_to_file
"""


import json


def serialize_and_save_to_file(data, filename):
    """
    data:
        the data to serialize
    filename:
        the json file to write in
    """
    data = {"name": "John Doe", "age": 30, "city": "New York"}
    with open("filename", "w") as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    filename:
        the json file to load from to create Data
    """
    with open("filename", "r") as file:
        loaded_data = json.load(file)
        return loaded_data
