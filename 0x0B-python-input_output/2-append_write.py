#!/usr/bin/python3
""" a function that appends a string at the end of a text file """


def append_write(filename="", text=""):
    """ a function tha append a file, returns the number of charc added """
    with open(filename, 'a', encoding='utf') as f:
        characters_written = f.write(text)
    return characters_written
