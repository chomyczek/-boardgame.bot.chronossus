from abc import ABC, abstractmethod


class IRewardedComponent(ABC):
    @abstractmethod
    def get_victory_points(self) -> int:
        raise NotImplementedError()
