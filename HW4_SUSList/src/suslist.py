"""
    Sorted Unique Square List
    Author: Taylor Hancock
    Class:  CS399
    Date:   03/25/2023

    NOTES:  Used GitHub Copilot for autocompletion of terms
"""


class SUSList(list):
    """ Datatype based on List, contains only sorted unique squares.
        I.e. the base-class' mutators that change the element order or add new elements, need to be overridden or disabled.
    """

    def __init__(self, *elements):
        """ Initializes a new List (optionally with the given elements)
        :type elements: *int
        """
        super().__init__()

        if elements is not None:
            self.extend(elements)

    def add(self, element: int) -> None:
        """
        Inserts the given element into the list, still keeping elements sorted and unique.
        If the element is not a square, it will be converted to its closest square: round(abs(element)**0.5)**2
        Only if the element is not already in the list, will be inserted.
        :type element: object
        """

        # If the element is not a square, convert it to its closest square
        if element ** 0.5 % 1 != 0:
            element = round(abs(element) ** 0.5) ** 2

        if element not in super():
            index = 0

            for value in super():
                if element < value:
                    index += 1
            super().insert(element, index)

    def extend(self, lst: list[int]) -> None:
        """
        Adds each element of the given list to this list, still keeping elements sorted and unique
        :type lst: list of integers
        """

        # Let add do all the work here
        for element in lst:
            self.add(element)

    def append(self, element) -> None:
        raise NotImplementedError

    def insert(self, index: int, element) -> None:
        raise NotImplementedError

    def reverse(self) -> None:
        raise NotImplementedError

    def sort(self, key=None, reverse=False) -> None:
        return None