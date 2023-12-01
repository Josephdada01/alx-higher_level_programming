#!/usr/bin/python3
"""
a Python script that takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response.
Requirements:
You must use the packages urllib and sys
You are not allow to import packages other than urllib and sys
The value of this variable is different for each request
You don’t need to check arguments passed to the script (number or type)
You must use a with statement
my personal solution:
with urllib.request.urlopen(url) as response:
x_request_id = response.headers.get("X-Request-Id")
print(x_request_id)
"""

import urllib.request
import sys


url = sys.argv[1]

if __name__ == "__main__":
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
