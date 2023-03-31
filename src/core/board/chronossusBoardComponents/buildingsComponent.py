
from enum import Enum

from src.core.exception import ActionFailedException


class BuildingComponent:

    class BuildingType(Enum):
        POWER_PLANT = 0
        FACTORY = 1
        LIFE_SUPPORT = 2
        LAB = 3
        SUPER_PROJECT = 15
        ANOMALY = 255

    class Building:
        def __init__(self, building_type: int, points: int):
            self.type = building_type
            self.points = points

    MAX_BUILDINGS_IN_POOL: int = 3
    _pools: dict[BuildingType, list[int]]= {}

    def __init__(self):
        self._pools[self.BuildingType.POWER_PLANT] = []
        self._pools[self.BuildingType.FACTORY] = []
        self._pools[self.BuildingType.LIFE_SUPPORT] = []
        self._pools[self.BuildingType.LAB] = []
        self._pools[self.BuildingType.SUPER_PROJECT] = []
        self._pools[self.BuildingType.ANOMALY] = []

    def add(self, building_type: BuildingType, points: int):
        pool = self._pools[building_type]
        if len(pool) >= self.MAX_BUILDINGS_IN_POOL:
            raise ActionFailedException()
        pool.push(points)

    def remove_anomaly(self):
        anomaly_pool = self._pools[self.BuildingType.ANOMALY]
        if not any(anomaly_pool):
            raise ActionFailedException()
        anomaly_pool.pop()


    def sum_victory_points(self) -> int:
        points = 0
        for pool in self._pools.values():
            points = sum(pool, sum)
        return points



