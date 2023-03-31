from src.core.base.type import ResourceType


class ResourcePoolComponent:
    _points: int
    _pool: dict[ResourceType, int]

    def __init__(self):
        self._points = 0
        self._pool = {}
        for resource in ResourceType:
            self._pool[resource] = 0

    def add(self, resource: ResourceType):
        self._pool[resource] += 1
        self._check_for_completed_set()

    def _check_for_completed_set(self) -> None:
        """
        Once it has at least one of all 4 Resource types, it discards one of each and gains 5 VPs.
        """
        if min(self._pool.values()) > 0:
            self._points += 5
            for resource in ResourceType:
                self._pool[resource] -= 1

    def get_victory_points(self) -> int:
        """
        Sum of points from recruiting workers.
        Calculate: 5VP if it has at least one of all 4 Resource types
        :return: Victory points value from collected resources.
        """
        return self._points
