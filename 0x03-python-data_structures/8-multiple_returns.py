#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None:
        return None
    else:
        length = len(sentence)
        first = sentence[0]
        result = (length, first)
        return result
