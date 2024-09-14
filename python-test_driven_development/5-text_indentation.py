#!/usr/bin/python3

"""
Define text_indentation function
"""


def text_indentation(text):

    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
    text (str): The input text to be formatted.

    Raises:
    TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Characters after which we need to add two new lines
    delimiters = ['.', '?', ':']

    # Initialize an empty result string
    result = ""

    # Flag to track if we're at the start of a new line
    new_line = True

    for char in text:
        # If we're at the start of a new line, skip any leading spaces
        if new_line and char == ' ':
            continue

        # Add the character to the result
        result += char

        # Reset the new_line flag
        new_line = False

        # If the character is a delimiter, add two new lines
        if char in delimiters:
            result += "\n\n"
            new_line = True

    # Print the result, stripping any trailing newlines
    print(result.rstrip())
