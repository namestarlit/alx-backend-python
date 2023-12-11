#!/usr/bin/env python3
"""A type-annotated function that crates a tuble from various data types"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Creates a Tuple of the given parameters

    Args:
        k (str): A string parameter
        v (int | float): An int or float paramater

    Returns:
        tuple: Returns a tuple

    """
    return (k, float(v ** 2))
