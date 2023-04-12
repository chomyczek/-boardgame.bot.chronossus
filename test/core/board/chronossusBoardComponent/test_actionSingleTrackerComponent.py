from _pytest.fixtures import fixture

from src.core.base.type import ActionTileType
from src.core.board.chronossusBoardComponent.actionSingleTrackerComponent import ActionSingleTrackerComponent


class TestActionSingleTrackerComponent:
    @fixture
    def action_single_tracker_component(self):
        actions = [ActionTileType.CONSTRUCT_LAB, ActionTileType.C01A]
        yield ActionSingleTrackerComponent(actions)

    def test_move(self, action_single_tracker_component):
        expected_step = action_single_tracker_component._step + 1
        action_single_tracker_component.move()
        assert action_single_tracker_component._step == expected_step

    def test_move_steps_exceeded(self, action_single_tracker_component):
        action_single_tracker_component._step = action_single_tracker_component.rule_max_steps
        expected_step = 0
        action_single_tracker_component.move()
        assert action_single_tracker_component._step == expected_step

    def test_get_current_action(self, action_single_tracker_component):
        expected_action = ActionTileType.CONSTRUCT_LAB
        assert action_single_tracker_component.get_current_action() == expected_action
