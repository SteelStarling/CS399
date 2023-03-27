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

    lst.add(9)
    assert lst == [1, 9], "Elements should be added in sorted order"

    lst.add(9)
    assert lst == [1, 9], "Adding an element that is already in the list should not change the list"

    lst.add(5)
    assert lst == [1, 4, 9], "Adding a non-square number should result in the closest square"

    lst.add(3)
    assert lst == [1, 4, 9], "Adding a non-square that evaluates to an element that already exists in the list should" \
                             "not change the list"

    lst.add(-16)
    assert lst == [1, 4, 9, 16], "Adding a negative of a square value should add the positive variant to the list"

    lst.add(-35)
    assert lst == [1, 4, 9, 16, 36], "Adding a negative non-square should add the square closest to the positive " \
                                     "equivalent to the list"


def test_extend():
    lst = SUSList()

    lst.extend([1, 4, 9])
    assert lst == [1, 4, 9], "Adding a correct SUSList to an empty list should result in an identical SUSList"

    lst.extend(lst)
    assert lst == [1, 4, 9], "Extending a SUSList with itself should return the same list"

    lst2 = SUSList()

    lst2.extend([5, 10, 17])
    assert lst2 == [4, 9, 16], "Extending an empty SUSList with non-squares should evaluate to all the nearest squares"

    lst2.extend([3, 8, 15])
    assert lst2 == [4, 9, 16], "Extending a SUSList with non-squares that evaluate to preexisting squares should not " \
                               "change the list"

    lst3 = SUSList()
    lst3.extend([9, 16, 4, 1])
    assert lst3 == [1, 4, 9, 16], "Extending a list by an unsorted list of squares should sort and add them to the list"



