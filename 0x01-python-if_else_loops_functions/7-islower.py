#!/usr/bin/python3
def islower(c):
    for i in range(97, 123):
        if chr(97) <= c <= chr(123):
            return True
        else:
            return False
