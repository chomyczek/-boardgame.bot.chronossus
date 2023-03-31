
from enum import Enum

from src.core.base.type import BuildingType
from src.core.exception import ActionFailedException


class BuildingComponent:

    class Building:
        def __init__(self, building_type: int, points: int):
            self.type = building_type
            self.points = points

    MAX_BUILDINGS_IN_POOL: int = 3
    _pools: dict[BuildingType, list[int]] = {}

    def __init__(self):
        self._pools[BuildingType.POWER_PLANT] = []
        self._pools[BuildingType.FACTORY] = []
        self._pools[BuildingType.LIFE_SUPPORT] = []
        self._pools[BuildingType.LAB] = []
        self._pools[BuildingType.SUPER_PROJECT] = []
        self._pools[BuildingType.ANOMALY] = []

    def add(self, building_type: BuildingType, points: int):
        pool = self._pools[building_type]
        if len(pool) >= self.MAX_BUILDINGS_IN_POOL:
            raise ActionFailedException(f'Pool of {building_type.value} is already full.')
        pool.append(points)

    def remove_anomaly(self):
        anomaly_pool = self._pools[BuildingType.ANOMALY]
        if not any(anomaly_pool):
            raise ActionFailedException(f'Pool of {BuildingType.ANOMALY} is empty.')
        anomaly_pool.pop()

    def sum_victory_points(self) -> int:
        points = 0
        for pool in self._pools.values():
            points = sum(pool, sum)
        return points



