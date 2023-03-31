from src.core.util.exception import ParadoxExceededException


class ParadoxTrackComponent:
    RULE_MAX_STEPS: int = 3
    _step: int

    def __init__(self):
        self._step = 0

    def move(self):
        self._step += 1
        if self._step > self.RULE_MAX_STEPS:
            self._step = 0
            raise ParadoxExceededException()
