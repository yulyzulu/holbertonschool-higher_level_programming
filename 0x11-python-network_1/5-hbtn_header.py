#!/usr/bin/python3
""" Module to execute functions"""

import requests
import sys

if __name__ == "__main__":

    req = requests.get(sys.argv[1])
    print(req.headers['X-Request-Id'])
