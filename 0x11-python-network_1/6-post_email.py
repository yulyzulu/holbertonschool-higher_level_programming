#!/usr/bin/python3
""" Module to execute functions"""

import requests
import sys

if __name__ == "__main__":

    req = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(req.text)