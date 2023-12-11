#!/usr/bin/env python3
"""using mypy to check types"""
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Create multiple copies of items in a tuple.

    Args:
        lst (Tuple): The input tuple containing items to be zoomed.
        factor (int, optional): The factor by which each item in the
        tuple will be zoomed.

    Returns:
        List: A list containing multiple copies of items from the input tuple
        zoomed by the specified factor.

    """
    zoomed_in: List = [
            item for item in lst
            for i in range(factor)
            ]
    return zoomed_in


array = [12, 72, 91]
zoom_2x = zoom_array(tuple(array))
zoom_3x = zoom_array(tuple(array), int(3.0))
