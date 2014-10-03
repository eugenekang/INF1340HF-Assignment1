#!/usr/bin/env python3

__author__ = 'Susan Sim' 'Archon Ren' 'Eugene Kang'
__email__ = "ses@drsusansim.org" "archon.ren@gmail.com" "eugene.yc.kang@gmail.com"

__copyright__ = "2014 Kang, Ren & Sim"
__license__ = "MIT License"

__status__ = "Prototype"

def decide_rps(player1, player2):
    """
    Checks who wins the rock paper scissors game

    :param player1: move of the first player
           player2: move of the second player
    :return:
        0 for tie
        1 for player1 win
        2 for player2 win
    :raises:
        TypeError if input is not string
        ValueError if string is not Rock or Paper or Scissors
    """
    #Defining the Rock, Paper, Scissors "scoring" dictionary
    rps_Dictionary = {}

    rps_Dictionary[("Scissors", "Scissors")] = 0
    rps_Dictionary[("Rock", "Rock")] = 0
    rps_Dictionary[("Paper", "Paper")] = 0

    rps_Dictionary[("Scissors", "Paper")] = 1
    rps_Dictionary[("Paper", "Rock")] = 1
    rps_Dictionary[("Rock", "Scissors")] = 1

    rps_Dictionary[("Scissors", "Rock")] = 2
    rps_Dictionary[("Paper", "Scissors")] = 2
    rps_Dictionary[("Rock", "Paper")] = 2

    #Function that trips errors if wrong input is entered, also returns result.
    if type(player1) is not str or type(player2) is not str:
        raise TypeError("Invalid type passed as parameter")
    elif player2 == "Rock" or player2 == "Paper" or player2 == "Scissors":
        if player1 == "Rock" or player1 == "Paper" or player1 == "Scissors":
            return rps_Dictionary[(player1, player2)]
        else:
                raise ValueError("Invalid value passed as parameter")
    else:
        raise ValueError("Invalid value passed as parameter")

