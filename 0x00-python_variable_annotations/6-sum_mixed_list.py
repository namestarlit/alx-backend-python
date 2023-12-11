#!/usr/bin/env python3
"""A type-annotated function that sums up elements of list elements"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """sums up elements of a list of mixed types

    Args:
        mxd_lst (list): A list containing integers and floats

    Returns:
        float: The sum of the elements of a mixed type list

    """
    return float(sum(mxd_lst))
