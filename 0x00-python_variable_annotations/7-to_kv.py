#!/usr/bin/env python3
from typing import Union, Optional, Tuple
"""
A module that takes a string and a int/float and returns a tupple
"""


def to_kv(k: str, v: Union[int | float]) -> Tuple[str | float]:
    """
    A func that takes a string and a int/float and returns a tuple
    Args:
        k: str
        v: float | int
    Returns:
        tup: tuple of k and v
    """
    v = v * v
    tup: Tuple[str, float] = (k, float(v))
    
    return tup
