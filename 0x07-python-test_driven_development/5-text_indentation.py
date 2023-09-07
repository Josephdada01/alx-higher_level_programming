#!/usr/bin/python3
"""
a function that print text with 2 new lines
after each of these character '.', '?', ':'
the text must be a string otherwise raise exception
"""


def text_indentation(text):
    """ a function that print text """
    if type(text) is not str:
        raise TypeError("text must be a string")
    for char in text:
        if char in ['.', '?', ':']:
            print(char)
            print("\n\n")
        else:
            print(char, end="")
