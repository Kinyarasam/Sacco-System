#!/usr/bin/env python3


import redis
import typing
from os import environ


class RedisClient:
    _client = None

    def __init__(self) -> None:
        self._client = redis.Redis()

    def isAlive(self) -> bool:
        try:
            return self._client.ping()
        except:
            return False

    def get(self, key=None) -> typing.Any:
        if key is None:
            return

        return self._client.get(key)

    def set(self, key, val, duration):
        if key is None:
            return

        return self._client.setex(key, duration*60, val)

    def delete(self, key=None):
        if key is not None:
            return self._client.delete(key)
