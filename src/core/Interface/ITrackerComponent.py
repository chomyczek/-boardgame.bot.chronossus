from abc import ABC, abstractmethod


class ITrackerComponent(ABC):
    rule_max_steps: int
    _step: int

    def __init__(self, max_steps):
        self.rule_max_steps = max_steps
        self._step = 0

    @abstractmethod
    def move(self):
        raise NotImplementedError()
