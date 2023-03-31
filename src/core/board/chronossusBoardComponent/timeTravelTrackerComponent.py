from src.core.Interface.IRewardedComponent import IRewardedComponent
from src.core.Interface.ITrackerComponent import ITrackerComponent


class TimeTravelTrackerComponent(ITrackerComponent, IRewardedComponent):

    def __init__(self):
        rule_max_steps = 6
        super().__init__(rule_max_steps)

    def move(self):
        if self._step < self.rule_max_steps:
            self._step += 1

    def get_victory_points(self) -> int:
        """
        Get 2VP for each step.
        :return: Victory points value from time travel track
        """
        return self._step * 2
