import pytest

from src.core.board.chronossusBoardComponent.paradoxTrackerComponent import ParadoxTrackerComponent
from src.core.util.exception import ParadoxExceededException


class TestParadoxTrackerComponent:
    def test_move(self):
        paradox_tracker_component = ParadoxTrackerComponent()
        expected_step = paradox_tracker_component._step + 1
        paradox_tracker_component.move()
        assert paradox_tracker_component._step == expected_step

    def test_move_steps_exceeded(self):
        paradox_tracker_component = ParadoxTrackerComponent()
        paradox_tracker_component._step = paradox_tracker_component.rule_max_steps
        expected_step = 0
        with pytest.raises(ParadoxExceededException):
            paradox_tracker_component.move()
        assert paradox_tracker_component._step == expected_step
