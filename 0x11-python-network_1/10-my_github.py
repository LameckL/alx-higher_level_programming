#!/usr/bin/python3
"""displays GitHub ID based on given credentials
Usage: ./10-my_github.py <GitHub username> <GitHub password>
  - uses Basic Authentication to access the ID
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    re = requests.get("https://api.github.com/user", auth=auth)
    print(re.json().get("id"))
