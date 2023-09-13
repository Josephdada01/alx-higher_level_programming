#!/usr/bin/python3
""" a module that reads a test file encode(UTF8) and print it to stdout"""


def read_file(filename=""):
    """ a function that read a textfile """
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end="")
