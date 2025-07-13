#!/usr/bin/env python3
from typing import List, Union
"""
A module that takes a list mxd_lst of integers and floats and
returns their sum as a float
"""



def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    A function that takes a list mxd_lst of integers and floats and
    returns their sum as a float
    Args:
        List: the mixed list to sum
    Returns:
        Float: The sum of the list
    """
    return float(sum(mxd_lst))
