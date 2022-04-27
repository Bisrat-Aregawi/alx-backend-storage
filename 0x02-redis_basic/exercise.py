#!/usr/bin/env python3
"""Module defines `Cache` class"""
import functools
import redis
from typing import Any, Optional, Union, Callable
from uuid import uuid4


def count_calls(method: Callable) -> Callable:
    """Decorator to print number of calls of method

    Args:
        method (Callable): variable representing decorated method

    Returns:
        Wrapper method that prints number of calls and returns value of
        wrapped method
    """
    @functools.wraps(method)
    def count_calls_wrapper(self, *args: Any, **kwargs: Any) -> Any:
        """Wrapper method for provided wrapped method"""
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)

    return count_calls_wrapper


class Cache:
    """Cache class"""
    DB_VAL_TYPS = Union[str, bytes, int, float]

    def __init__(self) -> None:
        """Constructor method for class `Cache`"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: DB_VAL_TYPS) -> str:
        """Store passed data in a unique key

        Args:
            data (str, bytes, int, float): data to save as value

        Returns:
            Unique key of type uuid4
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(
            self,
            key: str,
            fn: Optional[Callable] = None
    ) -> DB_VAL_TYPS:
        """Return decoded value at `key`

        Args:
            key (str): The key to retrieve data from
            fn (Callable): Function that decodes to utf-8

        Returns:
            decoded data from server
        """
        raw_data = self._redis.get(key)
        return fn(raw_data) if fn is not None else raw_data

    def get_str(self, data: bytes) -> str:
        """Return string casted data"""
        return data.decode('utf-8')

    def get_int(self, data: bytes) -> int:
        """Return integer casted data"""
        return int(data)
    pass
