#!/usr/bin/env python3

""" Assignment 1, Exercise 1, INF1340, Fall, 2014. Grade to gpa conversion

This module contains one function grade_to_gpa. It can be passed a parameter
that is an integer (0-100) or a letter grade (A+, A, A-, B+, B, B-, or FZ). All
other inputs will result in an error.

Example:
    $ python exercise1.py

"""

__author__ = 'Susan Sim' 'Archon Ren' 'Eugene Kang'
__email__ = "ses@drsusansim.org" "archon.ren@gmail.com" "eugene.yc.kang@gmail.com"

__copyright__ = "2014 Kang, Ren & Sim"
__license__ = "MIT License"

__status__ = "Prototype"

def grade_to_gpa(grade):
    """
    Return the UofT Graduate GPA for a given grade.

    :param:
        grade (integer or string): Grades to be converted
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
        if grade == "A+" or grade == "A" or grade == "A-" or grade == "B+" or grade == "B" or grade == "B-" or grade == "FZ":
            letter_grade = grade
        else:
            raise ValueError("Invalid Value. Please enter a letter grade from A+ to B-, or FZ")
    elif type(grade) is int:
        if grade >= 0 and grade <=100:
            letter_grade = mark_to_letter(grade)
        else:
            raise ValueError("Value entered is out of range")
    else:
        raise TypeError("Invalid type passed as parameter. Please enter an numeric, integer grade or letter grade")
    if letter_grade == "A+" or letter_grade == "A":
        gpa = 4.0
    elif letter_grade == "A-":
        gpa = 3.7
    elif letter_grade == "B+":
        gpa = 3.3
    elif letter_grade == "B":
        gpa = 3.0
    elif letter_grade == "B-":
        gpa = 2.7
    else:
        gpa = 0.0

    return gpa


def mark_to_letter(grade):
    """
    Returns the UofT Letter Grade for a given integer grade.

    :param:
        grade (integer): Grade to be converted
            Accepted values are 0-100.

    :return:
        string: The equivalent letter Grade
            Value is A+, A, A-, B+, B, B-, FZ
    """
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
    else:
        letter = "FZ"

    return letter

