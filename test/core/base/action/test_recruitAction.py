import pytest

from src.core.base.action.mineResourceAction import MineResourceAction
from src.core.base.action.recruitAction import RecruitAction
from src.core.base.type import ResourceType, WorkerType
from src.core.board.chronossusBoard import ChronossusBoard
from src.core.util.exception import PassActionsException


class TestRecruitAction:
    @pytest.mark.parametrize("worker",
                             [w for w in WorkerType])
    def test_execute(self, worker):
        board = ChronossusBoard()
        board.exosuits_pool.power_up_exosuits()
        action = RecruitAction(board)
        action.execute(worker)
        for w in WorkerType:
            if w == worker:
                assert board.workers_pool.get()[w] != 0
            else:
                assert board.workers_pool.get()[w] == 0

    def tests_execute_raise_pass(self):
        board = ChronossusBoard()
        action = RecruitAction(board)
        with pytest.raises(PassActionsException):
            action.execute(WorkerType.ENGINEER)

    @pytest.mark.parametrize("expected,populate",
                             [(
                              [WorkerType.GENIUS, WorkerType.ADMINISTRATOR, WorkerType.ENGINEER, WorkerType.SCIENTIST],
                              []),
                              (
                              [WorkerType.ADMINISTRATOR, WorkerType.ENGINEER, WorkerType.SCIENTIST, WorkerType.GENIUS],
                              [WorkerType.GENIUS]),
                              (
                              [WorkerType.GENIUS, WorkerType.ENGINEER, WorkerType.ADMINISTRATOR, WorkerType.SCIENTIST],
                              [WorkerType.ADMINISTRATOR, WorkerType.SCIENTIST]),
                              (
                              [WorkerType.ENGINEER, WorkerType.SCIENTIST, WorkerType.ADMINISTRATOR,WorkerType.GENIUS],
                              [WorkerType.GENIUS, WorkerType.GENIUS, WorkerType.ADMINISTRATOR]),
                              (
                              [WorkerType.GENIUS, WorkerType.ADMINISTRATOR, WorkerType.ENGINEER, WorkerType.SCIENTIST],
                              [WorkerType.SCIENTIST, WorkerType.SCIENTIST, WorkerType.SCIENTIST]),
                              (
                              [WorkerType.SCIENTIST, WorkerType.GENIUS, WorkerType.ADMINISTRATOR, WorkerType.ENGINEER],
                              [WorkerType.GENIUS, WorkerType.ADMINISTRATOR, WorkerType.ENGINEER]),
                              (
                              [WorkerType.GENIUS, WorkerType.ADMINISTRATOR, WorkerType.SCIENTIST, WorkerType.ENGINEER],
                              [WorkerType.ENGINEER, WorkerType.SCIENTIST, WorkerType.ENGINEER])
                              ])
    def test_get_priority(self, expected, populate):
        board = ChronossusBoard()
        action = RecruitAction(board)
        for worker in populate:
            board.workers_pool.add(worker)
        assert action.get_priority() == expected
