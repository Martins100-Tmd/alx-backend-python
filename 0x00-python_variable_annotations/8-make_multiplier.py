#!/usr/bin/env python3
'''
Task 9 module
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    return a float callable (function)
    '''
    return lambda x: x * multiplier
