from src.core.base.type import ActionTileType
from src.core.board.chronossusBoardComponent.actionSingleTrackerComponent import ActionSingleTrackerComponent
from src.core.board.chronossusBoardComponent.actionTrackerComponent import ActionTrackerComponent


class TestActionTrackerComponent:
    def test_trackers_populated_on_init(self):
        action_tracker_component = ActionTrackerComponent()
        assert len(action_tracker_component._trackers) == 4
        assert len(action_tracker_component._trackers[2]._tiles) == 5
        assert len(action_tracker_component._trackers[3]._tiles) == 5
        assert len(action_tracker_component._trackers[4]._tiles) == 5
        assert len(action_tracker_component._trackers[5]._tiles) == 4

    def test_move(self, mocker):
        mock_single_action_tracker = mocker.patch.object(ActionSingleTrackerComponent, "move")
        action_tracker_component = ActionTrackerComponent()
        action_tracker_component.move(2)
        assert mock_single_action_tracker.called

    def test_get_action(self, mocker):
        mock_single_action_tracker = mocker.patch.object(ActionSingleTrackerComponent, "get_current_action")
        action_tracker_component = ActionTrackerComponent()
        action_tracker_component.get_action(2)
        assert mock_single_action_tracker.called
