#!/usr/bin/env python3
"""
Task 1's module
"""
import asyncio
from typing import Coroutine, Any


async_generator = __import__("A").async_generator


async def async_comprehension() -> Coroutine[Any, Any, list[async_generator]]:
    """
    returns a list comprehension from a async generator fn
    """
    ls = [i async for i in async_generator()]
    return ls
