#!/usr/bin/env python3
"""Module defines `Cache` class"""
import redis
from typing import Union
from uuid import uuid4


class Cache:
    """Cache class"""
    def __init__(self) -> None:
        """Constructor method for class `Cache`"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store passed data in a unique key

        Args:
            data (str, bytes, int, float): data to save as value

        Returns:
            Unique key of type uuid4
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return key
    pass
