#!/usr/bin/env python3
"""A function with duck-typed annotations"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Retrives the first element of an Sequence

    Args:
        lst: An iterable data type

    Returns:
        Any: returns any first element of an iterable

    """
    return (lst[0] if lst else None)
