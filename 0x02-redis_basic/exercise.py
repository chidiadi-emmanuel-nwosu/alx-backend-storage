#!/usr/bin/env python3
""" exercise.py """
from typing import Union
import uuid
import redis


class Cache:
    """
    Cache class to store data using Redis
    """

    def __init__(self):
        """
        Initializes the Redis connection and flushes the database
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores the provided data in Redis with a UUID-based key

        Args:
        - data: The data to be stored

        Returns:
        - key: The generated UUID key used for storage
        """
        key: str = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
