#!/usr/bin/python3
def uppercase(str):
    casechangevalue = 32
    for i in str:
        if ord('a') <= ord(i) <= ord('z'):
            casechangevalue
            print("{}".format(chr(ord(i) - casechangevalue)), end='')
        else:
            print("{}".format(i), end='')
