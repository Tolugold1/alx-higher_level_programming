#!/usr/bin/python3
def print_last_digit(number):
    no = number
    if no < 0:
        no *= -1
    last_digit = no % 10
    print("{}".format(last_digit), end='')
    return last_digit
