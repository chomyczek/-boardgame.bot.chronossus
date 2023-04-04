from src.core.interface.IRewardedComponent import IRewardedComponent


class VictoryPointComponent(IRewardedComponent):
    """
    Worker pool component for chronossus board
    """

    _score: int

    def __init__(self):
        self._score = 0

    def add(self, vp: int) -> None:
        self._score += vp

    def get_victory_points(self) -> int:
        """
        Sum of points from pool.
        :return: Collected victory points value from.
        """
        return self._score
