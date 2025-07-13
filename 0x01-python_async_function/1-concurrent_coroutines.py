#!/usr/bin/env python3
"""
concurernt function
"""


import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Run wait_random coroutine n times with the specified max_delay
    and collect the results in the order they complete (ascending delays).

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay value that
        wait_random can wait.

    Returns:
        List[float]: A list of delays (floats), collected
        in the order of task completion.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    results = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        results.append(delay)
    return results
