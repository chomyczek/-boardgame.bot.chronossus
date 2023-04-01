import pytest

from src.core.board.chronossusBoardComponent.timeTravelTrackerComponent import TimeTravelTrackerComponent


class TestTimeTravelTrackerComponent:

    def test_move(self):
        time_travel_tracker_component = TimeTravelTrackerComponent()
        expected_step = time_travel_tracker_component._step + 1
        time_travel_tracker_component.move()
        assert time_travel_tracker_component._step == expected_step

    def test_move_steps_exceeded(self):
        time_travel_tracker_component = TimeTravelTrackerComponent()
        time_travel_tracker_component._step = time_travel_tracker_component.rule_max_steps
        expected_step = time_travel_tracker_component.rule_max_steps
        time_travel_tracker_component.move()
        assert time_travel_tracker_component._step == expected_step

    @pytest.mark.parametrize("steps,expected_vp",[(0,0), (2,4), (3,6), (20, 12)])
    def test_get_victory_points(self, steps,expected_vp):
        time_travel_tracker_component = TimeTravelTrackerComponent()
        for i in range(steps):
            time_travel_tracker_component.move()
        assert time_travel_tracker_component.get_victory_points() == expected_vp
