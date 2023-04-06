import pytest

from src.core.base.action.constructAction import ConstructAction
from src.core.base.component.buildingTile import BuildingTile
from src.core.base.type import BuildingType, BreakthroughType
from src.core.board.chronossusBoard import ChronossusBoard
from src.core.util.exception import PassActionsException


class TestConstructAction:

    @pytest.fixture()
    def powered_up_board(self):
        board = ChronossusBoard()
        board.exosuits_pool.power_up_exosuits()
        return board

    @pytest.mark.parametrize("construction_type", [BuildingType.LAB, BuildingType.FACTORY, BuildingType.ANOMALY, BuildingType.LIFE_SUPPORT, BuildingType.POWER_PLANT])
    def test_execute_no_super_project(self, construction_type, powered_up_board):
        vp = 1
        action = ConstructAction(powered_up_board, construction_type)
        action.execute(vp)
        assert powered_up_board.building_pool.get_victory_points() == vp

    def test_execute_super_project(self, powered_up_board):
        vp = 2
        powered_up_board.breakthroughs_pool.add(BreakthroughType.CIRCLE)
        action = ConstructAction(powered_up_board, BuildingType.SUPER_PROJECT)
        action.execute(vp)
        assert powered_up_board.building_pool.get_victory_points() == vp

    @pytest.mark.parametrize("construction_type", [building for building in BuildingType])
    def test_execute_raise_pass(self, construction_type):
        vp = 3
        board = ChronossusBoard()
        if construction_type == BuildingType.SUPER_PROJECT:
            board.breakthroughs_pool.add(BreakthroughType.TRIANGLE)
        action = ConstructAction(board, BuildingType.SUPER_PROJECT)
        with pytest.raises(PassActionsException):
            action.execute(vp)
        assert board.building_pool.get_victory_points() == 0

    def test_execute_failed_no_breakthroughs(self, powered_up_board, mocker):
        mock_failed_action = mocker.patch("src.core.base.action.failedAction.FailedAction.execute")
        vp = 4
        action = ConstructAction(powered_up_board, BuildingType.SUPER_PROJECT)
        action.execute(vp)
        assert mock_failed_action.called
        assert powered_up_board.building_pool.get_victory_points() == 0

    @pytest.mark.parametrize("construction_type", [building for building in BuildingType])
    def test_execute_failed_stack_full(self, construction_type, powered_up_board, mocker):
        mock_failed_action = mocker.patch("src.core.base.action.failedAction.FailedAction.execute")
        full_stack_mock = [BuildingTile(construction_type, 1) for i in
                           range(powered_up_board.building_pool.RULE_MAX_BUILDINGS_IN_POOL)]
        vp = 4
        action = ConstructAction(powered_up_board, construction_type)

        powered_up_board.building_pool._pool[construction_type] = full_stack_mock
        action.execute(vp)
        assert mock_failed_action.called
        assert powered_up_board.building_pool.get_victory_points() == powered_up_board.building_pool.RULE_MAX_BUILDINGS_IN_POOL



