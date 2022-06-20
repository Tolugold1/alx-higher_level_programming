#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        ans = []
        len = 0
        for i in range(x):
            if isinstance(my_list[i], int) == 1:
                ans.append(my_list[i])
                print("{:d}".format(my_list[i]), end='')
            else:
                pass
        for j in ans:
            len += 1
        print()
        return j
    except:
        print('IndexError: list index out of range')
