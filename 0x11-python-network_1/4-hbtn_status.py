#!/usr/bin/python3
"""
 Python script that takes in a URL and an email, sends a POST
"""


if __name__ == '__main__':
    import requests
    req = requests.get('https://alx-intranet.hbtn.io/status')
    print('Body response:\n\t- type: {}'.format(type(req.text)))
    print('\t- content: {}'.format(req.text))
