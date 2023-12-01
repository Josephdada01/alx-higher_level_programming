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
        data = r.read()
        print("Body response:")
        print("\t- type: {}".format(type(data)))
        print("\t- data: {}".format(data))
        print("\t- utf8 content: {}".format(data.decode('utf-8')))