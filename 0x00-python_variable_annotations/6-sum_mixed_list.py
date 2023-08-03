#!/usr/bin/env python3
'''
Task 7 module
'''
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[float, int]]) -> float:
    '''
    adds up list of float and int
    '''
    sum = 0.0
    count = 0

    while count < len(mxd_list):
        sum += float(mxd_list[count])
        count += 1
    return sum
