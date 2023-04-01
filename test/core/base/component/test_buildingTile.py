from src.core.base.component.buildingTile import BuildingTile
from src.core.base.type import BuildingType


class TestBuildingTile:
    def test_init(self):
        score = 123
        building_type = BuildingType.POWER_PLANT
        building = BuildingTile(building_type, score)
        assert building.type == building_type
        assert building.score == score
