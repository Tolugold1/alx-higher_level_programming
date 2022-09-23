#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
"""


if __name__ == '__main__':
    import urllib.request
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        file_body = res.read()
    print('Body response:\n\t - type: {}'.format(type(file_body)))
    print('\t - content: {}'.format(file_body))
    print('\t - utf8 content: {}'.format(file_body.decode('utf-8')))
