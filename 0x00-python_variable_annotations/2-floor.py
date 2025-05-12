#!/usr/bin/env python3
"""
A module that calculates the floor of a float
"""

import math


def floor(n: float) -> int:
    """
    a func that returns the floor of a float n

    Args:
        n (float): The number to find the floor of

    Returns:
        int: floor of the argument
    """
    fl = math.floor(n)
    return fl
