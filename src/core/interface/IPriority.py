import enum
from abc import ABC, abstractmethod


class IPriority(ABC):
    """
    Interface for actions with priority determinate
    """

    @abstractmethod
    def get_priority(self) -> list[enum]:
        """
        Get priority of the action
        :return: list of elements ordered by priority
        """
        raise NotImplementedError()
