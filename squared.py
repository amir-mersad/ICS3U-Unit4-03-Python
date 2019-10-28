#!/usr/bin/env python3

# Created by Amir Mersad
# Created on September 2019
# This program asks the user for a positive integer,
#  then gives the user the squared result


def main():
    # This function asks the user for a positive integer,
    #  then gives the user the squared result
    number = input("enter a number: ")
    result = 0
    counter = 0
    try:
        number = int(number)
        if number >= 0:
            for counter in range(number+1):
                result = counter ** 2
                print("{0}² = {1}".format(counter, result))
        else:
            print("number should be positive!")
    except(Exception):
        print("Wrong input!!!")


if __name__ == "__main__":
    main()
