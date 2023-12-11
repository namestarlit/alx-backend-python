#!/usr/bin/env python3
"""A type-annotated function that floors a float number"""
import math


def floor(n: float) -> int:
    """Floors a float into an integer

    Args:
        n (float): The number to floor

    Returns:
        int: The floored integer

    """
    return math.floor(n)
