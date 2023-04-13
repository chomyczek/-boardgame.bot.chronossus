import pytest

from src.core.base.action.removeAnomalyAction import RemoveAnomalyAction
from src.core.base.type import BuildingType, ResourceType
from src.core.board.chronossusBoard import ChronossusBoard
from src.core.board.chronossusBoardComponent.resourcePoolComponent import ResourceEnumPoolComponent
from src.core.util.exception import ActionFailedException


class TestRemoveAnomalyAction:
    def test_execute(self):
        board = ChronossusBoard()
        board.resources_pool.add(ResourceType.TITANIUM)
        board.resources_pool.add(ResourceType.TITANIUM)
        board.building_pool.add(BuildingType.ANOMALY, -3)
        action = RemoveAnomalyAction(board)
        action.execute()
        assert len(board.building_pool._pool[BuildingType.ANOMALY]) == 0
        assert board.building_pool.get_victory_points() == 0

    def test_execute_no_anomaly_action_failed(self):
        board = ChronossusBoard()
        board.resources_pool.add(ResourceType.TITANIUM)
        board.resources_pool.add(ResourceType.TITANIUM)
        action = RemoveAnomalyAction(board)
        with pytest.raises(ActionFailedException) as e:
            action.execute()
        assert str(e.value) == f"Pool of {BuildingType.ANOMALY.value} is empty."

    @pytest.mark.parametrize("resource_in_pool", [ResourceType.GOLD, ResourceType.TITANIUM, ResourceType.URANIUM, None])
    def test_execute_not_enough_resources_action_failed(self, resource_in_pool):
        anomaly_vp = -3
        anomaly_count = 1
        board = ChronossusBoard()
        board.building_pool.add(BuildingType.ANOMALY, anomaly_vp)
        if resource_in_pool:
            board.resources_pool.add(resource_in_pool)
        action = RemoveAnomalyAction(board)
        with pytest.raises(ActionFailedException) as e:
            action.execute()
        assert len(board.building_pool._pool[BuildingType.ANOMALY]) == anomaly_count
        assert board.building_pool.get_victory_points() == anomaly_vp
        assert str(e.value) == f"There is no {ResourceType.TITANIUM.value} resources."

    @pytest.mark.parametrize(
        "expected,resources_in_pool",
        [
            (
                [ResourceType.TITANIUM, ResourceType.GOLD],
                [ResourceType.GOLD, ResourceType.TITANIUM, ResourceType.URANIUM],
            ),
            (
                [ResourceType.TITANIUM, ResourceType.TITANIUM],
                [ResourceType.TITANIUM, ResourceType.TITANIUM, ResourceType.TITANIUM],
            ),
            (
                [ResourceType.TITANIUM, ResourceType.TITANIUM],
                [ResourceType.TITANIUM, ResourceType.NEUTRONIUM, ResourceType.TITANIUM],
            ),
            ([ResourceType.NEUTRONIUM], [ResourceType.NEUTRONIUM, ResourceType.GOLD, ResourceType.URANIUM]),
            ([ResourceType.TITANIUM, ResourceType.GOLD], []),
            ([ResourceType.URANIUM, ResourceType.TITANIUM], [ResourceType.URANIUM]),
            (
                [ResourceType.GOLD, ResourceType.TITANIUM],
                [
                    ResourceType.GOLD,
                    ResourceType.GOLD,
                    ResourceType.GOLD,
                    ResourceType.TITANIUM,
                    ResourceType.TITANIUM,
                    ResourceType.NEUTRONIUM,
                ],
            ),
        ],
    )
    def test_get_priority(self, expected, resources_in_pool):
        board = ChronossusBoard()
        test_resources_pool = ResourceEnumPoolComponent()
        for resource in resources_in_pool:
            board.resources_pool.add(resource)
            test_resources_pool.add(resource)
        action = RemoveAnomalyAction(board)
        priority = action.get_priority()
        assert priority == expected
        assert board.resources_pool.get() == test_resources_pool.get()
