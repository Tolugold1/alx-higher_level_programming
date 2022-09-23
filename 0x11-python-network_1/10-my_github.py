#!/usr/bin/python3
"""
Use the Github API to display a user's ID
"""

if __name__ == '__main__':
    import requests
    from sys import argv
    r = requests.get('https://api.github.com/user', auth=(argv[1], argv[2]))
    print(r.json().get('id'))
