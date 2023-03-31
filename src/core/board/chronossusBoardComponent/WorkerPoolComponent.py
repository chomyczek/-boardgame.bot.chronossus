from src.core.base.type import WorkerType


class WorkerPoolComponent:
    _points: int
    _pool: dict[WorkerType, int]

    def __init__(self):
        self._points = 0
        self._pool = {}
        for worker in WorkerType:
            self._pool[worker] = 0

    def add(self, worker: WorkerType):
        self._points += 1
        self._pool[worker] += 1
        self._check_for_completed_set()

    def _check_for_completed_set(self) -> None:
        """
        Once it has at least one of all 4 Worker types, it discards one of each and gains 5 VPs.
        """
        if min(self._pool.values()) > 0:
            self._points += 5
            for worker in WorkerType:
                self._pool[worker] -= 1

    def get_victory_points(self) -> int:
        """
        Sum of points from recruiting workers.
        Calculate: 1VP for recruiting, 5VP if it has at least one of all 4 Worker types
        :return: Victory points value from collected workers.
        """
        return self._points
