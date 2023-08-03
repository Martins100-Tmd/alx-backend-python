#!/usr/bin/env python3
'''
Task 7 module
'''
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[float, int]]) -> float:
    '''
    adds up list of float and int
    '''
    return float(sum(mxd_list))
