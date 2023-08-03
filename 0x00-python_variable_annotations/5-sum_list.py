#!/usr/bin/env python3
'''
Task 6 module
'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    '''
    adds up a float list
    '''
    sum: float = 0.0
    count = 0
    while count < len(input_list):
        sum += input_list[count]
        count += 1
    return sum
