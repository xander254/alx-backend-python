#!/usr/bin/env python3
"""
A module that  takes a list input_list of floats as
argument and returns their sum as a float
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    A func that takes a list input_list of floats as argument and
    returns their sum as a float

    Args:
        input_list (list[float]): A list containing float numbers
    Returns:
        float: sum of items in list
    """
    return sum(input_list)
