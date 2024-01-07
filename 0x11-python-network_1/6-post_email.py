#!/usr/bin/python3
"""send POST request to a given URL with a given email
Usage: ./6-post_email.py <URL> <email>
  - displays body of the response
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    re = requests.post(url, data=value)
    print(re.text)
