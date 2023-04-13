import pytest

from src.core.base.action.timeTravelAction import TimeTravelAction
from src.core.board.chronossusBoard import ChronossusBoard
from src.core.util.exception import ActionFailedException


class TestTimeTravelAction:
    def test_execute(self):
        board = ChronossusBoard()
        board.warp_token_pool.remove()
        action = TimeTravelAction(board)
        action.execute()
        assert board.time_travel_track._step == 1

    def test_execute_no_warp_token_action_failed(self):
        board = ChronossusBoard()
        action = TimeTravelAction(board)
        with pytest.raises(ActionFailedException) as e:
            action.execute()
        assert str(e.value) == "There is no warp tokens to remove from the Timelines."
