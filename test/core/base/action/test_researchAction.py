import pytest

from src.core.base.action.researchAction import ResearchAction
from src.core.base.component.die.researchShapeDie import ResearchShapeDie
from src.core.base.type import BreakthroughType
from src.core.board.chronossusBoard import ChronossusBoard
from src.core.util.exception import PassActionsException


class TestResearchAction:
    def test_execute(self, mocker):
        mocker.patch.object(ResearchShapeDie, "roll", return_value=BreakthroughType.CIRCLE)
        board = ChronossusBoard()
        board.exosuits_pool.power_up_exosuits()
        action = ResearchAction(board)
        action.execute()
        assert board.breakthroughs_pool.get()[BreakthroughType.CIRCLE] == 1
        assert board.breakthroughs_pool.get()[BreakthroughType.SQUARE] == 0
        assert board.breakthroughs_pool.get()[BreakthroughType.TRIANGLE] == 0

    def test_execute_no_exosuits_pass(self):
        board = ChronossusBoard()
        action = ResearchAction(board)
        with pytest.raises(PassActionsException):
            action.execute()
