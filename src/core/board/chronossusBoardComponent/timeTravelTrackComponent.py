class TimeTravelTrackComponent:
    MAX_STEPS: int = 6
    _step: int = 0

    def move(self):
        if self._step < self.MAX_STEPS:
            self._step += 1

    def get_victory_points(self) -> int:
        """
        Get 2VP for each step.
        :return: Victory points value from time travel track
        """
        return self._step * 2
