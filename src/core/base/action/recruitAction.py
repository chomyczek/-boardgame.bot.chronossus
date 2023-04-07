from src.core.base.action.failedAction import FailedAction
from src.core.base.type import WorkerType
from src.core.board.chronossusBoard import ChronossusBoard
from src.core.interface.IAction import IAction
from src.core.interface.IPriority import IPriority


class RecruitAction(IAction, IPriority):
    """
    When taking the Recruit Action, the Chronossus takes a
    Worker type it does not yet have, following the priority order
    below. If this Worker type is unavailable, it takes an available
    type, following the priority order. It does not receive its
    respective Recruit bonus ; however, it receives 1 VP
    regardless of the Worker type.
    Genius > Administrator > Engineer > Scientist
    Once it has at least one of all 4 Worker types, it discards
    one of each and gains 5 VPs.
    """

    _board: ChronossusBoard
    _failedAction: FailedAction

    def __init__(self, chronossus_board: ChronossusBoard):
        self._board = chronossus_board
        self._failedAction = FailedAction(chronossus_board)

    def execute(self, worker_type: WorkerType) -> None:
        """
        Execute recruit action
        :param worker_type: Type of worker to recruit
        """
        self._board.exosuits_pool.place_exosuit()
        self._board.workers_pool.add(worker_type)

    def get_priority(self) -> list[WorkerType]:
        """
        Worker type it does not yet have, following the priority order:
        Genius > Administrator > Engineer > Scientist
        :return: List of workers types ordered by priority
        """
        pool = self._board.workers_pool.get()
        general_priority = [WorkerType.GENIUS, WorkerType.ADMINISTRATOR, WorkerType.ENGINEER, WorkerType.SCIENTIST]
        priority = sorted(pool, key=lambda k: (pool[k], general_priority.index(k)))
        return priority
