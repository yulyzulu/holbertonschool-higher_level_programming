#!/usr/bin/python3
"""Module to execute functions"""

import urllib.request
from urllib import parse
import sys

if __name__ == "__main__":

    values = {'email': sys.argv[2]}
    data = parse.urlencode(values).encode('utf-8')
    url = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(url) as response:
        text = response.read().decode('utf-8')
        print("{}".format(text))
