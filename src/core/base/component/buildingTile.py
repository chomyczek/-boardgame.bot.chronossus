from src.core.base.type import BuildingType


class BuildingTile:
    def __init__(self, building_type: BuildingType, points: int):
        self.type = building_type
        self.score = points
