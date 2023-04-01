from src.core.base.type import WorkerType
from src.core.interface.IPoolComponent import IPoolComponent
from src.core.interface.IRewardedComponent import IRewardedComponent


class WorkerPoolComponent(IPoolComponent, IRewardedComponent):
    """
    Worker pool component for chronossus board
    """

    def __init__(self):
        super().__init__(WorkerType)

    def add(self, worker: WorkerType) -> None:
        self._score += 1
        super().add(worker)
        super().check_for_completed_set()

    def get_victory_points(self) -> int:
        """
        Sum of points from pool.
        :return: Collected victory points value from.
        """
        return self._score
