#!/usr/bin/env python3
"""using more involded type annotations"""
from typing import TypeVar, Mapping, Any, Union

T = TypeVar('T')


def safely_get_value(
        dct: Mapping,
        key: Any,
        default: Union[T, None] = None
        ) -> Union[Any, T]:
    """
    Safely retrieves a value from a dictionary based on a key.

    Args:
        dct (Mapping): The input dictionary.
        key (Any): The key to look up in the dictionary.
        default (Union[T, None]): The default value to return
        if the key is not found. Defaults to None.

    Returns:
        Union[Any, T]: The value associated with the key in the dictionary,
        or the default value if the key is not present.

    """
    return dct[key] if key in dct else default
