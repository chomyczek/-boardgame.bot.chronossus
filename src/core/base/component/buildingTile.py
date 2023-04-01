from src.core.base.type import BuildingType


class BuildingTile:
    """
    Model for building tile component
    """

    type: BuildingType
    score: int

    def __init__(self, building_type: BuildingType, points: int):
        self.type = building_type
        self.score = points
