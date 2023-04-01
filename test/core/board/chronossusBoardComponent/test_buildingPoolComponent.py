import itertools

import pytest

from src.core.base.type import BuildingType
from src.core.board.chronossusBoardComponent.buildingPoolComponent import BuildingPoolComponent
from src.core.util.exception import ActionFailedException


class TestBuildingPoolComponent:
    @pytest.mark.parametrize("building_type,score",
                             [(BuildingType.ANOMALY, -5), (BuildingType.POWER_PLANT, 1), (BuildingType.LAB, 2),
                              (BuildingType.FACTORY, 3), (BuildingType.LIFE_SUPPORT, 8),
                              (BuildingType.SUPER_PROJECT, 7)])
    def test_add(self, building_type, score):
        building_pool_component = BuildingPoolComponent()
        building_pool_component.add(building_type, score)
        for building in BuildingType:
            expected = 0
            if building == building_type:
                expected = 1
            assert len(building_pool_component._pool[building]) == expected
            if building == building_type:
                assert building_pool_component._pool[building][0].score == score

    @pytest.mark.parametrize("building_type",
                             [BuildingType.ANOMALY, BuildingType.LAB, BuildingType.POWER_PLANT, BuildingType.FACTORY,
                              BuildingType.LIFE_SUPPORT, BuildingType.SUPER_PROJECT])
    def test_add_to_full_pool(self, building_type):
        building_pool_component = BuildingPoolComponent()
        for i in range(building_pool_component.RULE_MAX_BUILDINGS_IN_POOL):
            building_pool_component.add(building_type, 1)
        with pytest.raises(ActionFailedException) as e:
            building_pool_component.add(building_type, 2)
        assert str(e.value) == f'Pool of {building_type.value} is already full.'

    @pytest.mark.parametrize("pool_count", range(1, BuildingPoolComponent.RULE_MAX_BUILDINGS_IN_POOL + 1))
    def test_remove_anomaly(self, pool_count: int):
        building_pool_component = BuildingPoolComponent()
        for i in range(pool_count):
            building_pool_component.add(BuildingType.ANOMALY, -3)
        building_pool_component.remove_anomaly()
        assert len(building_pool_component._pool[BuildingType.ANOMALY]) == pool_count - 1

    def test_remove_anomaly_empty_pool(self):
        building_pool_component = BuildingPoolComponent()
        with pytest.raises(ActionFailedException) as e:
            building_pool_component.remove_anomaly()
        assert str(e.value) == f'Pool of {BuildingType.ANOMALY.value} is empty.'

    @pytest.mark.parametrize("pool_count,building_type", list(
        itertools.product(range(BuildingPoolComponent.RULE_MAX_BUILDINGS_IN_POOL + 1),
                          [building for building in BuildingType])))
    def test_get_victory_points_one_type(self, pool_count: int, building_type):
        vp = 2
        building_pool_component = BuildingPoolComponent()
        for i in range(pool_count):
            building_pool_component.add(building_type, vp)
        assert building_pool_component.get_victory_points() == pool_count * vp

    @pytest.mark.parametrize("pool_count", range(BuildingPoolComponent.RULE_MAX_BUILDINGS_IN_POOL + 1))
    def test_get_victory_points_all_types(self, pool_count: int):
        vp = 3
        type_values = [building for building in BuildingType]
        building_pool_component = BuildingPoolComponent()
        for i in range(pool_count):
            for building in type_values:
                building_pool_component.add(building, vp)
        assert building_pool_component.get_victory_points() == pool_count * vp * len(type_values)
