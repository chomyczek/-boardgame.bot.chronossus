from src.core.base.action.failedAction import FailedAction
from src.core.board.chronossusBoard import ChronossusBoard
from src.core.interface.IAction import IAction
from src.core.util.exception import ActionFailedException


class TimeTravelAction(IAction):

    def __init__(self, chronossus_board: ChronossusBoard):
        self._board = chronossus_board
        self._failedAction = FailedAction(chronossus_board)

    def execute(self) -> None:
        try:
            self._board.warp_token_pool.add()
            self._board.time_travel_track.move()
        except ActionFailedException:
            self._failedAction.execute()
