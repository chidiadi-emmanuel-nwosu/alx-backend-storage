#!/usr/bin/env python3
""" exercise.py """
from functools import wraps
from typing import Union, Callable, Optional
import uuid
import redis


def count_calls(method: Callable) -> Callable:
    """ decorator """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


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

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[bytes, str, int]:
        """
        Retrieves the value associated with the given key from the cache.

        Args:
        - key: A string representing the key to retrieve
               the value from the cache.
        - fn: An optional callable function to convert the retrieved value.
              Defaults to None if no conversion needed.

        Returns:
        - Union[bytes, str, int]: The retrieved value from the cache.
                                 If a conversion function is provided,
                                 it returns the converted value.
        """
        value = self._redis.get(key)

        if not value:
            return value

        if fn:
            value = fn(value)

        return value

    def get_str(self, key: str) -> str:
        """
        Retrieves the value associated with the given key from the cache
        and returns it as a string.

        Args:
        - key: A string representing the key to retrieve the
               value from the cache.

        Returns:
        - Union[bytes, str]: The retrieved value from the cache as a string.
        """
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """
        Retrieves the value associated with the given key from the cache
        and returns it as a string.

        Args:
        - key: A string representing the key to retrieve
               the value from the cache.

        Returns:
        - Union[bytes, str]: The retrieved value from the cache as an int.
        """
        return self.get(key, lambda x: int(x.decode('utf-8')))
