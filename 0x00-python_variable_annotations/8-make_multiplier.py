#!/usr/bin/env python3
"""A type-annotated fuction that returns a function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    # use 'lambda parameters: expression' syntax to return a lambda function
    return lambda x: x * multiplier
