#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
"""


if __name__ == '__main__':
    import requests
    from sys import argv

    url = argv[1]
    req = requests.get(url)
    if req.status_code < 400:
        print(req.text)
    else:
        print('Error code: {}'.format(req.status_code))
