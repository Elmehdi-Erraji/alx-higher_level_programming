#!/usr/bin/python3
"""
4-inherits_from module
"""


def inherits_from(obj, a_class):
    """
    inherits_from - Checks if an object is an inherited instance of a class.
    Args:
        obj: The object to check.
        a_class: The class to match the type of obj to.
    Returns: If obj is an inherited instance of a_class - True,
            Otherwise - False.
    """
    return isinstance(obj, a_class) and type(obj) != a_class
