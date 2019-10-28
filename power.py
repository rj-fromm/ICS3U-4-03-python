#!/usr/bin/env python3

# Created by: RJ Fromm
# Created on: Oct 2019
# This program multiplies numbers together


def main():

    number = int(input("Please enter a number : "))

    for counter in range(number + 1):
        square = counter**2
        print("{0}² = {1}".format(counter, square))


if __name__ == "__main__":
    main()
