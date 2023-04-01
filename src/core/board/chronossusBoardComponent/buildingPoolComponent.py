from src.core.base.component.buildingTile import BuildingTile
from src.core.base.type import BuildingType
from src.core.interface.IRewardedComponent import IRewardedComponent
from src.core.util.exception import ActionFailedException


class BuildingPoolComponent(IRewardedComponent):
    """
    Buildings and anomaly pool component for chronossus board
    """

    RULE_MAX_BUILDINGS_IN_POOL: int = 3
    _pool: dict[BuildingType, list[BuildingTile]]

    def __init__(self):
        self._pool = {}
        for building in BuildingType:
            self._pool[building] = []

    def add(self, building_type: BuildingType, score: int) -> None:
        """
        Add new building to building pool
        :param building_type: Type of building to add to pool
        :param score: score of added building
        """
        pool = self._pool[building_type]
        if len(pool) >= self.RULE_MAX_BUILDINGS_IN_POOL:
            raise ActionFailedException(f"Pool of {building_type.value} is already full.")

        pool.append(BuildingTile(building_type.value, score))

    def remove_anomaly(self) -> None:
        """
        Remove one anomaly from building pool
        """
        anomaly_pool = self._pool[BuildingType.ANOMALY]
        if not any(anomaly_pool):
            raise ActionFailedException(f"Pool of {BuildingType.ANOMALY.value} is empty.")
        anomaly_pool.pop()

    def get_victory_points(self) -> int:
        """
        Sum value of all collected buildings.
        :return: Victory points value from buildings pools.
        """
        points_sum = 0
        for tiles in self._pool.values():
            points = [t.score for t in tiles]
            points_sum = sum(points, points_sum)
        return points_sum
