#!/usr/bin/python3
"""
    -  takes your GitHub credentials (username and password) 
    - uses the GitHub API to display your id
"""

import requests
from sys import argv

if __name__ == '__main__':
    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(argv[1], argv[2]))
    try:
        print(response.json().get("id"))
    except Exception:
        print("Not a valid JSON")
