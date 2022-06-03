#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv


def main():
    number_of_arg = len(argv)
    if number_of_arg != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    if argv[2] != '+' or argv[2] != '-' or argv[2] != '*' or argv[2] != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(argv[1])
    b = int(argv[2])
    if argv[2] == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif argv[2] == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif argv[2] == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif argv[2] == '/':
        print("{} / {} = {}".format(a, b, div(a, b)))


if __name__ == "__main__":
    main()
