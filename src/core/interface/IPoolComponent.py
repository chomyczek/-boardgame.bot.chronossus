import enum
from abc import ABC, abstractmethod


class IPoolComponent(ABC):
    """
    Interface for pool components on boards
    """

    _score: int
    _pool: dict[enum, int]
    _pool_type: enum

    def __init__(self, pool_type: enum):
        self._score = 0
        self._pool = {}
        self._pool_type = pool_type
        for member in self._pool_type:
            self._pool[member] = 0

    @abstractmethod
    def add(self, member: enum.Enum) -> None:
        """
        Abstract method of adding 1 component to subtype of pool
        :param member: Subtype od the pool
        """
        self._pool[member] += 1

    @abstractmethod
    def get(self):
        raise NotImplementedError()

    def check_for_completed_set(self) -> None:
        """
        Once it has at least one of all types, it discards one of each and gains 5 VPs.
        """
        if min(self._pool.values()) > 0:
            self._score += 5
            for member in self._pool_type:
                self._pool[member] -= 1
