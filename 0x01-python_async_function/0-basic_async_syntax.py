#!/usr/bin/env python3
import asyncio
import random
"""
a module that runs using asyc and random
"""


async def wait_random(max_delay: int = 10) -> float:
    """
    Await a task in a random amount of seconds and respond
    Args:
        max_delay: int, max seconds to wait
    Returns:
            time: float. time taken to complete the task
    """
    time: float = random.uniform(0, max_delay)
    await asyncio.sleep(time)
    return time
