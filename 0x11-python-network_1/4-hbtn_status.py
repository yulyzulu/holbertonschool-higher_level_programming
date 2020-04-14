#!/usr/bin/python3
""" Module to execute functions"""

import requests

if __name__ == "__main__":

    req = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("	- type: {}".format(type(req.text)))
    print("	- content: {}".format(req.text))
