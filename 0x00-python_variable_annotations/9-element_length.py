#!/usr/bin/env python3
"""A type-annotated function that uses list compression"""
from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns length of of each element of an iterable

    Args:
        lst: an iterable it can be a list

    Returns:
        list: A list containing the length of each element

    """
    return [(i, len(i)) for i in lst]
