#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
"""


if __name__ == '__main__':
    import requests
    from sys import argv

    if len(argv) == 1:
        q = ""
    else:
        q = argv[2]
    req = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        data = req.json()
        if data:
            print('[{}] {}'.format(data.get('id'), data.get('name')))
        else:
            print('No result')
    except:
        print('Not a valid JSON')
