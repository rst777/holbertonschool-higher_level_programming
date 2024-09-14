#!/usr/bin/python3
"""Define text_indentation function"""


def text_indentation(text):
    """prints a text with 2 new lines after
    each of these characters: ., ? and :"""
    if not type(text) is str:
        raise TypeError("text must be a string")

    special_chr = {'.', ':', '?'}
    begin = 0
    for end in range(len(text)):
        if text[end] in special_chr:
            line = text[begin:end + 1] + "\n\n"
            begin = end + 1
            print("{}".format(line.strip(" ")), end="")
    if begin <= end:
        line = text[begin:end + 1]
        print("{}".format(line.strip(" ")), end="")
