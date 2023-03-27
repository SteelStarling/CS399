"""
    Tests for the SUSList class.
    Author: Taylor Hancock
    Class:  CS399
    Date:   03/25/2023

    NOTES:  Used GitHub Copilot for autocompletion of assert info and terms
"""


import pytest
from suslist import SUSList

def test_add():
    lst = SUSList()

    lst.add(1)
    assert lst == [1], "Adding 1 to an empty list should result in [1]"

    lst.add(5)
    assert lst == [1, 4], "Adding a non-square number should result in the closest square"

    lst.add(2)
    assert lst == [1, 2, 4], "Elements should be added in sorted order"

    lst.add(2)
    assert lst == [1, 2, 4], "Adding an element that is already in the list should not change the list"

def test_extend():
    assert False

