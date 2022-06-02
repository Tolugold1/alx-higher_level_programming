#!/usr/bin/python3
from sys import argv


def main():
    i = 0
    for j in range(1, len(argv)):
        i += int(argv[j])
    print('{}'.format(i))


if __name__ == "__main__":
    main()
