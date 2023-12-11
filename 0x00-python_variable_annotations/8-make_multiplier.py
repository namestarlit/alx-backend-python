#!/usr/bin/env python3
"""A type-annotated fuction that returns a function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """A function that returns a function

    Args:
        multiplier (float): A float number used as a multiplier

    Returns:
        function: A callable function

    """
    # use 'lambda parameters: expression' syntax to return a lambda function
    return lambda x: x * multiplier
