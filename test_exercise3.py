#!/usr/bin/env python3

""" Module to test exercise3.py """

import pytest
from exercise3 import decide_rps


def test_checksum():
    """
    Inputs that are the correct format
    """
    assert decide_rps("Rock", "Paper") == 2
    assert decide_rps("Scissors", "Scissors") == 0
    assert decide_rps("Rock", "Scissors") == 1
    assert decide_rps("Paper", "Scissors") == 2


def test_invalid_input():
    """
    invalid input
    """
    with pytest.raises(TypeError):
        decide_rps("Rock", 214)

    with pytest.raises(ValueError):
        decide_rps("Rok", "Scissors")

test_checksum()
