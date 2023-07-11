#!/usr/bin/python3
"""
3-is_kind_of_class module
"""


def is_kind_of_class(obj, a_class):
    """
    is_kind_of_class: Check if an object is an instance,
                    or inherited instance of a class.
    Args:
        obj: The object to check.
        a_class: The class to match the type of obj to.
    Returns: If obj is an instance or inherited instance of a_class - True,
            Otherwise - False.
    """
    return isinstance(obj, a_class)
