#!/usr/bin/python3
def common_elements(set_1, set_2):
    if set_1 and set_2:
        new_set = set_1.intersection(set_2)
        return new_set
    else:
        return []
