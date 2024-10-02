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

    with open("filename", "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    filename:
        the json file to load from to create Data
    """
    with open("filename", "r", encoding="utf-8") as f:
        data = json.load(f)
        return data
