#!/usr/bin/python3
"""Module to execute functions"""

import requests
import sys

if __name__ == "__main__":

    req = requests.get(sys.argv[1])
    if (req.status_code < 400):
        print(req.text)
    else:
        err_code = req.status_code
        print("Error code: {}".format(err_code))
