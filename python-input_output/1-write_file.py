#!/usr/bin/python3
"""Contains to the method write to the file"""


def write_file(filename="", text=""):
    """function that write a string at the end of a
    text file (UTF8) and returns the number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
