from src.core.base.action.timeTravelAction import TimeTravelAction
from src.core.board.chronossusBoard import ChronossusBoard


class TestTimeTravelAction:
    def test_execute(self):
        board = ChronossusBoard()
        board.warp_token_pool.remove()
        action = TimeTravelAction(board)
        action.execute()
        assert board.time_travel_track._step == 1

    def test_execute_no_warp_token_action_failed(self, mocker):
        mock_failed_action = mocker.patch("src.core.base.action.failedAction.FailedAction.execute")
        board = ChronossusBoard()
        action = TimeTravelAction(board)
        action.execute()
        assert mock_failed_action.called
