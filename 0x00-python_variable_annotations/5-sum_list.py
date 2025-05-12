#!/usr/bin/env python3
"""
A module that  takes a list input_list of floats as argument and returns their sum as a float
"""


def sum_list(input_list: list[float]) -> float:
    """
    A func that takes a list input_list of floats as argument and 
    returns their sum as a float

    Args: 
      float: items in the list
    Returns:
        float: sum of items in list
    """
    total: float = sum(input_list)
    return total
