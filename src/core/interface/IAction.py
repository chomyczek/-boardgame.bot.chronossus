from abc import ABC, abstractmethod


class IAction(ABC):
    """
    Interface for action
    """

    @abstractmethod
    def execute(self, *args) -> None:
        """
        execute action
        :param args: various arguments
        """
        raise NotImplementedError()
