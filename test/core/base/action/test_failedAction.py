from src.core.base.action.failedAction import FailedAction
from src.core.board.chronossusBoard import ChronossusBoard


class TestFailedAction:
    def test_execute(self):
        board = ChronossusBoard()
        action = FailedAction(board)
        action.execute()
        assert board.victory_points_pool.get_victory_points() == 1
