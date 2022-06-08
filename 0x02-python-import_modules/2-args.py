#!/usr/bin/python3
from sys import argv


def main():
    number_of_arg = len(argv) - 1
    if number_of_arg < 1:
        print("{} arguments.".format(number_of_arg))
    elif number_of_arg == 1:
        print("{} argument:".format(number_of_arg))
        print("{}: ".format(number_of_arg) + argv[1])
    elif number_of_arg > 1:
        print("{} arguments:".format(number_of_arg))
        for i in range(1, len(argv)):
            print('{}: {}'.format(i, argv[i]))


if __name__ == "__main__":
    main()
