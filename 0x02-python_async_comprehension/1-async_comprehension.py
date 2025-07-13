#!/usr/bin/env python3
"""
Run async comprehensions
"""


import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random float numbers from async_generator
    using async comprehension.
    Returns:
        List[float]: A list of 10 float values collected asynchronously.
    """
    return [value async for value in async_generator()]
