#!/usr/bin/env python3
"""A module parameters and return values with the appropriate types"""


from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """check element length"""
    return [(i, len(i)) for i in lst]
