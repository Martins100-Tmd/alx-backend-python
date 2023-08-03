#!/usr/bin/env python3
'''
Task 11 module
'''


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''
    return the first element of lst or None
    '''
    if lst:
        return lst[0]
    else:
        return None
