#!/usr/bin/env python3

__author__ = 'Susan Sim' 'Archon Ren' 'Eugene Kang'
__email__ = "ses@drsusansim.org" "archon.ren@gmail.com" "eugene.yc.kang@gmail.com"

__copyright__ = "2014 Kang, Ren & Sim"
__license__ = "MIT License"

__status__ = "Prototype"


def decide_rps(player1, player2):
    """
    Determines who wins the rock paper scissors game

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
    #Check if the correct type is passed (string)
    if type(player1) is str and type(player2) is str:
        #Set all input to uppercase and ensure the correct values are passed (ROCK, PAPER, or SCISSORS) for p1+2
        if player1.upper() == "ROCK" or player1.upper() == "PAPER" or player1.upper() == "SCISSORS":
            if player2.upper() == "ROCK" or player2.upper() == "PAPER" or player2.upper() == "SCISSORS":
                #Returns the result of the rps_Dictionary with the input passed from player 1 and 2 as
                #the keys for the tuple.
                return rps_Dictionary[(player1.upper(), player2.upper())]
            else:
                raise ValueError("Invalid Value for Player 2. Please enter ROCK, PAPER, or SCISSORS")
        else:
            raise ValueError("Invalid Value for Player 1. Please enter ROCK, PAPER, or SCISSORS")
    else:
        raise TypeError("Invalid type. Please enter a string.")

#Defining the Rock, Paper, Scissors "scoring" dictionary
    """
    Dictionary storing the different possible outcomes and "scores" for the Rock, Paper, Scissors game.
    Different combinations are stored as a tuple in the compound-key format. (player1, player2)=return_value
    """
rps_Dictionary = {
    ("SCISSORS", "SCISSORS"): 0,
    ("ROCK", "ROCK"): 0,
    ("PAPER", "PAPER"): 0,
    ("SCISSORS", "PAPER"): 1,
    ("PAPER", "ROCK"): 1,
    ("ROCK", "SCISSORS"): 1,
    ("SCISSORS", "ROCK"): 2,
    ("ROCK", "PAPER"): 2,
    ("PAPER", "SCISSORS"): 2
}




