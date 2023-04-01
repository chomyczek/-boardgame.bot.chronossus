from abc import ABC, abstractmethod


class IRewardedComponent(ABC):
    """
    Interface for components that are worth victory points
    """

    @abstractmethod
    def get_victory_points(self) -> int:
        """
        Abstract method of get_victory_points
        :return: Number of victory points that component is worth
        """
        raise NotImplementedError()
