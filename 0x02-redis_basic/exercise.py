#!/usr/bin/env python3
"""Module defines `Cache` class"""
import redis
from typing import Optional, Union, Callable
from uuid import uuid4


class Cache:
    """Cache class"""
    DB_VAL_TYPS = Union[str, bytes, int, float]

    def __init__(self) -> None:
        """Constructor method for class `Cache`"""
        self._redis = redis.Redis()
        self._redis.flushdb()

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
