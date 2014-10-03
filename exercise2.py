#!/usr/bin/env python3

"""
    Perform a checksum on a UPC

    Assignment 1, Exercise 2, INF1340 Fall 2014
"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line


def checksum(upc):
    """
    Checks if the digits in a UPC is consistent with checksum

    :param upc: a 12-digit universal product code
    :return:
        Boolean: True, checksum is correct
        False, otherwise
    :raises:
        TypeError if input is not a string
        ValueError if string is the wrong length (with error string stating how many digits are over or under
    """
    check_sum = 0
    if type(upc) is not str:
        raise TypeError("Invalid type passed as parameter")
    elif len(upc) != 12:
        if len(upc) < 12:
            raise ValueError("Your UPC is " + str(12-len(upc)) + " digits too short.")
        if len(upc) > 12:
            raise ValueError("Your UPC is " + str(len(upc)-12) + " digits too long.")
    else:
        digits = list(upc)
        for i in range(0, 11):
            if i % 2 != 0:
                check_sum += int(digits[i])
            else:
                check_sum += int(digits[i])*3
        check_sum %= 10
        check_sum = 10 - check_sum
        check_sum %= 10
        if check_sum == int(digits[11]):
            return True
        else:
            return False



