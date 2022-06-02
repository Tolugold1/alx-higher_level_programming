#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div


def main():
    number_of_arg = len(argv) - 1
    if number_of_arg < 3 or number_of_arg > 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
    else:
        if argv[1] != '+' or argv[1] != '-' or argv[1] != '*' or argv[1] != '/':
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        else:
            if argv[1] == '+':
                print("{} + {} = {}".format(argv[0], argv[2], add(int(argv[0]), int(argv[2]))))
            elif argv[1] == '-':
                print("{} + {} = {}".format(argv[0], argv[2], sub(int(argv[0]), int(argv[2]))))
            elif argv[1] == '*':
                print("{} + {} = {}".format(argv[0], argv[2], mul(int(argv[0]), int(argv[2]))))
            elif argv[1] == '/':
                print("{} + {} = {}".format(argv[0], argv[2], div(int(argv[0]), int(argv[2]))))


if __name__ == "__main__":
    main()
