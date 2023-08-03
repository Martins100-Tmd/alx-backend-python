#!/usr/bin/env python3
'''
Task 10 module
'''
from typing import List, Tuple, Sequence, Iterable

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''
    returns element length
    '''
    return [(i, len(i)) for i in lst]
