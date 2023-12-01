#!/usr/bin/python3
"""
a Python script that fetches https://alx-intranet.hbtn.io/status
You must use the package urllib
You are not allowed to import any packages other than urllib
The body of the response must be displayed like the following
example (tabulation before -)
You must use a with statement
"""
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as r:
        content = r.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))
