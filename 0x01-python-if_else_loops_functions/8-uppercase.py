#!/usr/bin/python3
def uppercase(str):
    for i in str:
        new = chr(ord(i) - 32)
        print("{}".format(new), end='')
