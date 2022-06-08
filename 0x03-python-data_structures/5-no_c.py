#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        list_str = []
        new_string = ""
        for i in my_string:
            list_str.append(i)
        for j in list_str:
            if j == 'c':
                list_str.remove("c")
            elif j == 'C':
                list_str.remove("C")
        new_string = new_string.join(list_str)
        return new_string
    else:
        return None
