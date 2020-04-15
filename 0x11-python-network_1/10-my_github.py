#!/usr/bin/python3
"""Script that takes Github credentials (username and password)
and uses the Github API to display id"""

from requests.auth import HTTPDigestAuth
import requests
import sys

if __name__ == "__main__":

    req = requests.get('https://api.github.com/use\
r', auth=(sys.argv[1], sys.argv[2]))
    print(req.text)
    try:
        json_id = req.json()
        print("{}".format(json_id['id']))
    except:
        print(None)
