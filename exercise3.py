#!/usr/bin/env python3


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

    if type(player1) is not str or type(player2) is not str:
        raise TypeError("Invalid type passed as parameter")
    elif player2 == "Rock" or player2 == "Paper" or player2 == "Scissors":
        if player1 == "Rock" or player1 == "Paper" or player1 == "Scissors":
            if player1 == player2:
                return 0
            elif (player1 == "Rock" and player2 == "Paper") or (player1 == "Paper" and player2 == "Scissors") or (
                    player1 == "Scissors" and player2 == "Rock"):
                return 2
            else:
                return 1
        else:
                raise ValueError("Invalid value passed as parameter")
    else:
        raise ValueError("Invalid value passed as parameter")

