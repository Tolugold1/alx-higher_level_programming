#!/usr/bin/python3
from sys import argv


def main():
    number_of_arg = len(argv) - 1
    i = 0
    if number_of_arg < 1:
        print("{}".format(i))
    elif number_of_arg == 1:
        print("{}".format(i + int(argv[1])))
    elif number_of_arg > 1:
        for j in range(1, len(argv)):
            i += int(argv[j])
        print('{}'.format(i))


if __name__ == "__main__":
    main()
