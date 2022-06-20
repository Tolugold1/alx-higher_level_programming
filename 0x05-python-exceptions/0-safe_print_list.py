#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        len = 0
        for i in my_list:
            len += 1
        if x > len:
            x = len
        for j in range(x):
            print(my_list[j], end="")
        print()
        return x
    except:
        print()
