#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


def main():
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, add(a, b)))


if __name__ == "__main__":
    main()


def submain():
    a = 10
    b = 5
    print("{} - {} = {}".format(a, b, sub(a, b)))


if __name__ == "__main__":
    submain()


def mulmain():
    a = 10
    b = 5
    print("{} * {} = {}".format(a, b, mul(a, b)))


if __name__ == "__main__":
    mulmain()


def dmain():
    a = 10
    b = 5
    print("{} / {} = {}".format(a, b, div(a, b)))


if __name__ == "__main__":
    dmain()
