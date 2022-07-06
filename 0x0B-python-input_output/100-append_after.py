#!/usr/bin/python3
"""
function that inserts a line of text to a file,
after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """function that inserts a line of text"""
    with open(filename, 'r') as f:
        text = f.readlines()

    with open(filename, 'w') as f:
        string = ''
        for i in text:
            string += i
            if search_string in i:
                string += new_string
        f.write(string)
