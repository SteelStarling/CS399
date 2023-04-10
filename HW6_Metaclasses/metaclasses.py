""" This module contains a metaclass that adds a default docstring to all callables without one.
    Author: Taylor Hancock
    Date:   04/09/2023
    Notes:  Text completion was provided by GitHub Copilot
"""


from typing import Any, Type


class DocMeta(type):
    def __new__(mcs: Any, name: str, bases: tuple, attr: dict) -> Type:
        new_class = type.__new__(mcs, name, bases, attr)
        for val in attr:
            # Fetch attribute
            attr_val = getattr(new_class, val)
            # Only run if callable and has no docstring
            if callable(attr_val) and attr_val.__doc__ is None:
                attr_val.__doc__ = "No documentation available."

        return new_class


class MyClass(metaclass=DocMeta):
    class_var = "I am a class variable."

    def my_method(self) -> None:
        """A method that prints a message."""
        print("I am a method.")

    def my_undocumented_method(self) -> None:
        print("I am an undocumented method.")


if __name__ == "__main__":
    my_obj = MyClass()
    print(MyClass.class_var)  # prints "I am a class variable."
    my_obj.my_method()  # prints "I am a method."
    my_obj.my_undocumented_method()  # prints "I am an undocumented method."

    print(help(my_obj.my_method))  # prints ".... A method that prints a message ...."
    print(MyClass.my_method.__doc__)  # prints "A method that prints a message."

    print(help(my_obj.my_undocumented_method))  # prints " .... No documentation available ...."
    print(MyClass.my_undocumented_method.__doc__)  # prints "No documentation available."
