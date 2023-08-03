#!/usr/bin/env python3
'''
Task 13 module
'''
from typing import Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> Tuple:
    '''
    Make a list outta tuple
    '''
    zoomed_in: Tuple = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = tuple([12, 72, 91])

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
