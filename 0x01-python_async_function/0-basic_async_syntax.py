#!/usr/bin/env python3
'''
Task 0's module
'''
from typing import Coroutine, Any
import random
import time
import asyncio


async def wait_random(max_delay=10):
    '''
    wait for a delay time and returns the
    delay time
    '''
    rand = random.uniform(0, max_delay)
    await asyncio.sleep(rand)
    return rand
