#!/usr/bin/env python3
'''
Task 8 module
'''
from typing import Union, Tuple
from math import pow


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''
    return tuple of str and float
    '''
    if type(v).__name__ == 'int':
        return (k, int(pow(v, 2)))
    return (k, float(pow(v, 2)))
