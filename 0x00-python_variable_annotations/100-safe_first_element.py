#!/usr/bin/env python3
"""Aottated function chat checks safety"""


from typing import Sequence, Any, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    if lst:
        return lst[0]
    else:
        return None
