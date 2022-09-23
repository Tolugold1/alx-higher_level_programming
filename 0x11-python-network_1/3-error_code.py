#!/usr/bin/python3
"""
 Python script that takes in a URL and an email, sends a POST
"""


if __name__ == '__main__':
    import urllib.request
    from sys import argv
    import urllib.error

    url = argv[1]
    try:
        with urllib.request.urlopen(url) as res:
            file_body = res.read()
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))
