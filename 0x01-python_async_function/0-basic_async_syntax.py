#!/usr/bin/env python3
import asyncio
import random
"""
a module that runs using asyc and random
"""


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay
    between 0 and max_delay seconds.
    Args:
        max_delay (int): Maximum number of seconds to wait.
        Default is 10.
    Returns:
        float: The actual number of seconds the coroutine
        waited (randomly chosen).
    This coroutine should be awaited.
    """
    time: float = random.uniform(0, max_delay)
    await asyncio.sleep(time)
    return time
