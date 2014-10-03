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
    if type(player1) is str and type(player2) is str:
        if player1.upper() == "ROCK" or player1.upper() == "PAPER" or player1.upper() == "SCISSORS":
            if player2.upper() == "ROCK" or player2.upper() == "PAPER" or player2.upper() == "SCISSORS":
                return rps_Dictionary[(player1.upper(), player2.upper())]
            else:
                raise ValueError("Invalid Value for Player 2. Please enter ROCK, PAPER, or SCISSORS")
        else:
            raise ValueError("Invalid Value for Player 1. Please enter ROCK, PAPER, or SCISSORS")
    else:
        raise TypeError("Invalid type. Please enter a string.")

#Defining the Rock, Paper, Scissors "scoring" dictionary
rps_Dictionary = {}

rps_Dictionary[("SCISSORS", "SCISSORS")] = 0
rps_Dictionary[("ROCK", "ROCK")] = 0
rps_Dictionary[("PAPER", "PAPER")] = 0

rps_Dictionary[("SCISSORS", "PAPER")] = 1
rps_Dictionary[("PAPER", "ROCK")] = 1
rps_Dictionary[("ROCK", "SCISSORS")] = 1

rps_Dictionary[("SCISSORS", "ROCK")] = 2
rps_Dictionary[("PAPER", "SCISSORS")] = 2
rps_Dictionary[("ROCK", "PAPER")] = 2


