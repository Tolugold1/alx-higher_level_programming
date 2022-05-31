#!/usr/bin/python3
def uppercase(str):
    casechangevalue = 32
    strg = ""
    for i in str:
        if ord('a') <= ord(i) <= ord('z'):
            casechangevalue = 32
            t = chr(ord(i) - casechangevalue)
        else:
            casechangevalue = 0
            t = i
        strg = strg + t
    print("{}".format(strg))
