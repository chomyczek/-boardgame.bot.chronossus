from src.core.board.chronossusBoard import ChronossusBoard
from src.core.interface.IAction import IAction


class FailedAction(IAction):
    """
    If an Action cannot be taken because there are no available
    Action spaces, it does not place an Exosuit and receives 1 VP
    instead. If an Action can be taken but cannot be performed
    (examples are given in each Action’s section), the Chronossus
    places the Exosuit and receives the 1 VP instead of the
    normal effect of the Action.
    """

    _board: ChronossusBoard

    def execute(self) -> None:
        """
        Execute failed action
        """
        self._board.victory_points_pool.add(1)

    def __init__(self, chronossus_board: ChronossusBoard):
        self._board = chronossus_board
