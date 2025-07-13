#!/usr/bin/env python3
from collections.abc import Callable
"""
A module that takes a float multiplier as argument and
returns a function that multiplies a float by multiplier
"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """a func that a function that multiplies a float by multiplier"""
    def multiplier_func(value: float) -> float:
        """a function that multiplies a float by multiplier"""
        return value * multiplier
    return multiplier_func
