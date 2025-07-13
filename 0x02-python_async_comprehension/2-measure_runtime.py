#!/usr/bin/env python3
"""
Run async comprehensions
"""


import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Run async_comprehension 4 times in parallel and measure total runtime.
    Returns:
        float: total elapsed time in seconds
    """
    start_time = time.perf_counter()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    )

    end_time = time.perf_counter()

    return end_time - start_time
