import pytest

from src.core.base.action.mineResourceAction import MineResourceAction
from src.core.base.type import ResourceType
from src.core.board.chronossusBoard import ChronossusBoard
from src.core.util.exception import PassActionsException


class TestMineResourceAction:
    @pytest.mark.parametrize("resources",
                             [[None, None], [None, ResourceType.NEUTRONIUM], [ResourceType.URANIUM, None],
                              [ResourceType.TITANIUM, ResourceType.TITANIUM]])
    def test_execute(self, resources: ResourceType):
        board = ChronossusBoard()
        board.exosuits_pool.power_up_exosuits()
        action = MineResourceAction(board)
        action.execute(resources[0], resources[1])
        for resource in ResourceType:
            if resource in resources:
                assert board.resources_pool.get()[resource] != 0
            else:
                assert board.resources_pool.get()[resource] == 0

    def tests_execute_raise_pass(self):
        board = ChronossusBoard()
        action = MineResourceAction(board)
        with pytest.raises(PassActionsException):
            action.execute(ResourceType.TITANIUM, ResourceType.GOLD)

    @pytest.mark.parametrize("expected,populate",
                             [(
                              [ResourceType.NEUTRONIUM, ResourceType.URANIUM, ResourceType.GOLD, ResourceType.TITANIUM],
                              []),
                              (
                              [ResourceType.URANIUM, ResourceType.GOLD, ResourceType.TITANIUM, ResourceType.NEUTRONIUM],
                              [ResourceType.NEUTRONIUM]),
                              (
                              [ResourceType.URANIUM, ResourceType.TITANIUM, ResourceType.NEUTRONIUM, ResourceType.GOLD],
                              [ResourceType.NEUTRONIUM, ResourceType.GOLD]),
                              (
                              [ResourceType.URANIUM, ResourceType.TITANIUM, ResourceType.GOLD, ResourceType.NEUTRONIUM],
                              [ResourceType.NEUTRONIUM, ResourceType.NEUTRONIUM, ResourceType.GOLD]),
                              (
                              [ResourceType.NEUTRONIUM, ResourceType.URANIUM, ResourceType.GOLD, ResourceType.TITANIUM],
                              [ResourceType.TITANIUM, ResourceType.TITANIUM, ResourceType.TITANIUM]),
                              (
                              [ResourceType.TITANIUM, ResourceType.NEUTRONIUM, ResourceType.URANIUM, ResourceType.GOLD],
                              [ResourceType.NEUTRONIUM, ResourceType.GOLD, ResourceType.URANIUM]),
                              (
                              [ResourceType.NEUTRONIUM, ResourceType.URANIUM, ResourceType.TITANIUM, ResourceType.GOLD],
                              [ResourceType.GOLD, ResourceType.TITANIUM, ResourceType.GOLD])
                              ])
    def test_get_priority(self, expected, populate):
        board = ChronossusBoard()
        action = MineResourceAction(board)
        for resource in populate:
            board.resources_pool.add(resource)
        prio = action.get_priority()
        exp = expected
        assert action.get_priority() == expected
