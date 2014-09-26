#!/usr/bin/env python3

""" Assignment 1, Exercise 1, INF1340, Fall, 2014. Grade to gpa conversion

This module contains one function grade_to_gpa. It can be passed a parameter
that is an integer (0-100) or a letter grade (A+, A, A-, B+, B, B-, or FZ). All
other inputs will result in an error.

Example:
    $ python exercise1.py

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line


def grade_to_gpa(grade):
    """
    Returns the UofT Graduate GPA for a given grade.

    :param:
        grade (integer or string): Grade to be converted
            If integer, accepted values are 0-100.
            If string, accepted values are A+, A, A-, B+, B, B-, FZ

    :return:
        float: The equivalent GPA
            Value is 0.0-4.0

    :raises:
        TypeError if parameter is not a string or integer
        ValueError if parameter is out of range
    """

    letter_grade = ""
    gpa = 0.0

    if type(grade) is str:
        if grade == "A+" or grade == "A" or grade == "A-" or grade == "B+" or grade == "B" or grade == "B-" or grade == "C+" or grade == "C" or grade == "C-" or grade == "D+" or grade == "D-" or grade == "D" or grade == "FZ":
            letter_grade = grade
        else:
            raise ValueError("Invalid value passed as parameter")
    elif type(grade) is int:
        if 100 >= grade >= 0:
            letter_grade = mark_to_letter(grade)
        else:
            raise ValueError("Invalid value passed as parameter")
    else:
        raise TypeError("Invalid type passed as parameter")

    if letter_grade == "A+":
        gpa = 4.0
    elif letter_grade == "A":
        gpa = 4.0
    elif letter_grade == "A-":
        gpa = 3.7
    elif letter_grade == "B+":
        gpa = 3.3
    elif letter_grade == "B":
        gpa = 3.0
    elif letter_grade == "B-":
        gpa = 2.7
    elif letter_grade == "C+":
        gpa = 2.3
    elif letter_grade == "C":
        gpa = 2.0
    elif letter_grade == "C-":
        gpa = 1.7
    elif letter_grade == "D+":
        gpa = 1.3
    elif letter_grade == "D":
        gpa = 1.0
    elif letter_grade == "D-":
        gpa = 0.7
    else:
        gpa = 0.0

    return gpa


def mark_to_letter(grade):
    if grade >= 90:
        letter = "A+"
    elif grade >= 85:
        letter = "A"
    elif grade >= 80:
        letter = "A-"
    elif grade >= 77:
        letter = "B+"
    elif grade >= 73:
        letter = "B"
    elif grade >= 70:
        letter = "B-"
    elif grade >= 67:
        letter = "C+"
    elif grade >= 63:
        letter = "C"
    elif grade >= 60:
        letter = "C-"
    elif grade >= 57:
        letter = "D+"
    elif grade >= 53:
        letter = "D"
    elif grade >= 50:
        letter = "D-"
    else:
        letter = "FZ"

    return letter