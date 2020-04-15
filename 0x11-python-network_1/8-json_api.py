#!/usr/bin/python3
"""Script that takes in a letter and sends a POST request with the
letter as a parameter"""

import requests
import sys

if __name__ == "__main__":

    if (len(sys.argv) == 2):
        req = requests.post('http://0.0.0.0:5000/search_use\
r', data={'q': sys.argv[1]})

        if (req.json is not None):
            try:
                json_dic = req.json()
                print("[{}] {}".format(json_dic['id'], json_dic['name']))
            except ValueError:
                print("Not a valid JSON")
    else:
        print('No result')
