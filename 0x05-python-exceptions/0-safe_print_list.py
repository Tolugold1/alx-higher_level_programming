#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        len = 0
        for j in range(x):
            print(my_list[j], end="")
            len += 1
        print()
    except Exception:
        print()
    return len
