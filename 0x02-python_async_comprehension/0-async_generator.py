#!/usr/bin/env python3
"""
Coroutine that yields 10 random floats between 0 and 10,
one every second (asynchronously)
"""


import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Coroutine that yields 10 random floats between 0 and 10,
    one every second (asynchronously).
    Returns:
        AsyncGenerator[float, None]: An asynchronous
        generator yielding float values
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
