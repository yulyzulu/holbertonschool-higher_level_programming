#!/usr/bin/python3
"""Module to execute functions"""

import urllib.request
import sys

if __name__ == "__main__":

    url = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(url) as response:
            text = response.read().decode('utf-8')
            print("{}".format(text))
    except urllib.error.HTTPError as e:
        err_code = e.code
        print("Error code: {}".format(err_code))
