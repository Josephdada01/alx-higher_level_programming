#!/usr/bin/python3
""" a module that writes a string to a text file encode UTF8 """


def write_file(filename="", text=""):
    """ this write string to a text file and return the number of character"""
    with open(filename, 'w', encoding='utf-8') as f:
        characters_written = f.write(text)
    return characters_written
