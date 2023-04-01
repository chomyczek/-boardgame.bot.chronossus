from src.core.base.type import BreakthroughType
from src.core.interface.IPoolComponent import IPoolComponent
from src.core.interface.IRewardedComponent import IRewardedComponent
from src.core.util.exception import ActionFailedException


class BreakthroughPoolComponent(IPoolComponent, IRewardedComponent):
    def add(self, breakthrough: BreakthroughType):
        super().add(breakthrough)

    def __init__(self):
        super().__init__(BreakthroughType)

    def remove_any(self) -> None:
        if all(b == 0 for b in self._pool.values()):
            raise ActionFailedException("There is no breakthroughs.")
        breakthrough_type = max(self._pool, key=self._pool.get)
        self._pool[breakthrough_type] -= 1

    def get_victory_points(self) -> int:
        """
        Calculate: 1 VP per Breakthrough, plus 2 additional VPs for each complete shape set.
        :return: Victory points value from breakthrough pool
        """
        # 1 VP per Breakthrough
        points = sum(self._pool.values())
        # 2 VPs for each complete shape set
        points += min(self._pool.values()) * 2
        return points
