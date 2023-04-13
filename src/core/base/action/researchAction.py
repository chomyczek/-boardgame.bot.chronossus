from src.core.base.component.die.researchShapeDie import ResearchShapeDie
from src.core.board.chronossusBoard import ChronossusBoard
from src.core.interface.IAction import IAction


class ResearchAction(IAction):
    """
    When using the Research Action, only roll the
    shape die, taking any Breakthrough of the rolled
    shape.
    """

    _die: ResearchShapeDie

    def __init__(self, chronossus_board: ChronossusBoard):
        self._board = chronossus_board
        self._die = ResearchShapeDie()

    def execute(self) -> None:
        """
        Execute research action
        """
        self._board.exosuits_pool.place_exosuit()
        shape = self._die.roll()
        self._board.breakthroughs_pool.add(shape)
