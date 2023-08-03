#!/usr/bin/env python3
'''
Task 10 module
'''


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''
    returns element length
    '''
    return [(i, len(i)) for i in lst]
