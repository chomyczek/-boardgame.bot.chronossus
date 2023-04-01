from abc import ABC, abstractmethod


class IRewardedComponent(ABC):
    """
    Interface for components that are worth victory points
    """

    @abstractmethod
    def get_victory_points(self) -> int:
        raise NotImplementedError()
