#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
"""


if __name__ == '__main__':
    import requests
    from sys import argv

    url = argv[1]
    req = requests.get(argv[1])
    print('{}'.format(req.headers.get('X-Request-Id')))
