#!/usr/bin/python3
def max_integer(my_list=[]):
    if (my_list):
        max_int = 0
        for i in range(len(my_list)):
            if max_int < my_list[i]:
                max_int = my_list[i]
        return max_int
    else:
        return None
