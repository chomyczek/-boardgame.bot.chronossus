from src.core.base.action.failedAction import FailedAction
from src.core.board.chronossusBoard import ChronossusBoard
from src.core.interface.IAction import IAction
from src.core.util.exception import ActionFailedException


class TimeTravelAction(IAction):
    """
    When “Time Travel” is selected, it removes
    any one Warp tile from the past Timeline
    tile where the Chronossus has the most
    Warp tiles (oldest if tied). If a Warp tile was
    removed the Chronossus advances one
    step on the Time Travel track.
    REMOVE ANOMALY
    The Chronossus does not place any Exosuits on a Time
    Travel Action. If there are no Warp tiles left on the Timeline,
    the Action is failed, and it scores 1 VP as usual.
    """

    _board: ChronossusBoard
    _failedAction: FailedAction

    def __init__(self, chronossus_board: ChronossusBoard):
        self._board = chronossus_board
        self._failedAction = FailedAction(chronossus_board)

    def execute(self) -> None:
        """
        Execute time travel action
        """
        try:
            self._board.warp_token_pool.add()
            self._board.time_travel_track.move()
        except ActionFailedException:
            self._failedAction.execute()
