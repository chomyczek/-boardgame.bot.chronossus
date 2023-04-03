import enum
from abc import ABC, abstractmethod


class IPriority(ABC):
    @abstractmethod
    def get_priority(self) -> list[enum]:
        raise NotImplementedError()
