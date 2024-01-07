#!/usr/bin/python3
"""sends POST request to http://0.0.0.0:5000/search_user with a given letter
Usage: ./8-json_api.py <letter>
  - letter sent as the value of the variable `q`
  - sends `q=""` if no letter provided
"""
import sys
import requests


if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": letter}

    re = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        response = re.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
