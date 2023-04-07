from src.core.base.action.failedAction import FailedAction
from src.core.base.component.researchShapeDie import ResearchShapeDie
from src.core.board.chronossusBoard import ChronossusBoard
from src.core.interface.IAction import IAction
from src.core.util.exception import ActionFailedException


class ResearchAction(IAction):
    _die: ResearchShapeDie
    _failedAction: FailedAction

    def __init__(self, chronossus_board: ChronossusBoard):
        self._board = chronossus_board
        self._die = ResearchShapeDie()
        self._failedAction = FailedAction(chronossus_board)

    def execute(self) -> None:
        self._board.exosuits_pool.place_exosuit()
        shape = self._die.roll()
        self._board.breakthroughs_pool.add(shape)
