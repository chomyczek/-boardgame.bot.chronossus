import enum
from abc import ABC, abstractmethod


class IDie(ABC):
    """
    Interface for die components on the board
    """

    @abstractmethod
    def roll(self) -> enum:
        """
        Roll the die.
        """
        raise NotImplementedError()
