#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
"""


if __name__ == '__main__':
    import requests
    from sys import argv

    url = argv[1]
    req = requests.post(url, data={'email': argv[2]})
    print('{}'.format(req.text))
