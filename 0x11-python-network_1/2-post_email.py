#!/usr/bin/python3
"""
 Python script that takes in a URL and an email, sends a POST
"""


if __name__ == '__main__':
    import urllib.request
    from sys import argv
    import urllib.parse
    url = argv[1]
    value = {'email': argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as res:
        email_sent = res.read()
    print('Your email is: {}'.format(email_sent.decode('utf-8')))
