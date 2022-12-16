#!/usr/bin/python3
"""
    - takes in a letter
    - sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter
"""

import requests
from sys import argv

if __name__ == '__main__':
    url = "http://0.0.0.0:5000/search_user"
    data = {"q": argv[1][0] if len(argv) > 1 else ""}
    response = requests.post(url, data=data)
    try:
        display = response.json()
        if not display:
            print("No result")
        else:
            print("[{}] {}".format(display.get("id"), display.get("name")))
    except Exception:
        print("Not a valid JSON")
