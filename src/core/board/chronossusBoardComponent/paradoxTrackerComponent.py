from src.core.interface.ITrackerComponent import ITrackerComponent
from src.core.util.exception import ParadoxExceededException


class ParadoxTrackerComponent(ITrackerComponent):
    def __init__(self):
        rule_max_steps = 3
        super().__init__(rule_max_steps)

    def move(self):
        self._step += 1
        if self._step > self.rule_max_steps:
            self._step = 0
            raise ParadoxExceededException()
