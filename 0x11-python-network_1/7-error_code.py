#!/usr/bin/python3
"""send request to a given URL, then displays the response body
Usage: ./7-error_code.py <URL>
  - handles HTTP errors
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    re = requests.get(url)
    if re.status_code >= 400:
        print("Error code: {}".format(re.status_code))
    else:
        print(re.text)
