#!/usr/bin/env python3
"""A type-annotated function that sums elements of a list"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """sums elements of an input list

    Args:
        input_list (list): A list of floats parameter

    Returns:
        float: The sum of list elements

    """
    return sum(input_list)
