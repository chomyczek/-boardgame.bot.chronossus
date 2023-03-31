import enum
from abc import ABC, abstractmethod


class IPoolComponent(ABC):
    _points: int
    _pool: dict[enum, int]
    _pool_type: enum

    def __init__(self, pool_type: enum, check_for_set=True):
        self._points = 0
        self._pool = {}
        self._pool_type = pool_type
        self._check_for_set = check_for_set
        for member in self._pool_type:
            self._pool[member] = 0

    @abstractmethod
    def add(self, member: enum.Enum):
        self._pool[member] += 1
        if self._check_for_set:
            self.check_for_completed_set()

    def check_for_completed_set(self) -> None:
        """
        Once it has at least one of all types, it discards one of each and gains 5 VPs.
        """
        if min(self._pool.values()) > 0:
            self._points += 5
            for member in self._pool_type:
                self._pool[member] -= 1



