#!/usr/bin/env python3
"""
Task 0's module
"""
import asyncio
from typing import Iterable
import random


async def async_generator() -> Iterable[float]:
    """
    yields a random number range 0 - 10
    """
    for i in range(10):
        rand = random.uniform(0, 10)
        await asyncio.sleep(1)
        yield rand
