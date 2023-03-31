from src.core.exception import ParadoxExceededException


class ParadoxTrackComponent:
    MAX_STEPS: int = 3
    _step: int = 0

    def move(self):
        self._step += 1
        if self._step > self.MAX_STEPS:
            self._step = 0
            raise ParadoxExceededException()

    def get_victory_points(self) -> int:
        """
        There is no points for paradoxes.
        :return: Always returns 0
        """
        return 0
