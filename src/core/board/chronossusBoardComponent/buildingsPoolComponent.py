from src.core.base.component.BuildingTile import BuildingTile
from src.core.base.type import BuildingType
from src.core.exception import ActionFailedException


class BuildingPoolComponent:
    RULE_MAX_BUILDINGS_IN_POOL: int = 3
    _pools: dict[BuildingType, list[BuildingTile]]

    def __init__(self):
        self._pools = {}
        for building in BuildingType:
            self._pools[building] = []

    def add(self, building_type: BuildingType, points: int) -> None:
        pool = self._pools[building_type]
        if len(pool) >= self.RULE_MAX_BUILDINGS_IN_POOL:
            raise ActionFailedException(f'Pool of {building_type.value} is already full.')

        pool.append(BuildingTile(building_type, points))

    def remove_anomaly(self) -> None:
        anomaly_pool = self._pools[BuildingType.ANOMALY]
        if not any(anomaly_pool):
            raise ActionFailedException(f'Pool of {BuildingType.ANOMALY} is empty.')
        anomaly_pool.pop()

    def get_victory_points(self) -> int:
        """
        Sum value of all collected buildings.
        :return: Victory points value from buildings pools.
        """
        points_sum = 0
        for tiles in self._pools.values():
            points = [t.points for t in tiles]
            points_sum = sum(points, points_sum)
        return points_sum



