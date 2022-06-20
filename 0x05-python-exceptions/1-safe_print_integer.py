#!/usr/bin/python3
def safe_print_integer(value):
    try:
        i = isinstance(value, int)
        if i == 1:  # 1 for true, 0 for false
            print("{:d}".format(value))
            return True
        else:
            return False
    except TypeError:
        print()
