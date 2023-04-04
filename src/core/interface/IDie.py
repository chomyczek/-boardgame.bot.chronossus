import enum
from abc import ABC, abstractmethod


class IDie(ABC):
    @abstractmethod
    def roll(self) -> enum:
        raise NotImplementedError()
