from src.core.base.action.failedAction import FailedAction
from src.core.base.type import WorkerType
from src.core.board.chronossusBoard import ChronossusBoard
from src.core.interface.IAction import IAction
from src.core.interface.IPriority import IPriority
from src.core.util.exception import ActionFailedException


class RecruitAction(IAction, IPriority):
    _board: ChronossusBoard
    _failedAction: FailedAction

    def __init__(self, chronossus_board: ChronossusBoard):
        self._board = chronossus_board
        self._failedAction = FailedAction(chronossus_board)

    def execute(self, worker_type: WorkerType) -> None:
        try:
            self._board.exosuits_pool.place_exosuit()
            self._board.workers_pool.add(worker_type)
        except ActionFailedException:
            self._failedAction.execute()

    def get_priority(self) -> list[WorkerType]:
        priority = []
        pool = self._board.workers_pool.get()
        i = 0
        for worker in [WorkerType.GENIUS, WorkerType.ADMINISTRATOR, WorkerType.ENGINEER, WorkerType.SCIENTIST]:
            if pool[worker] == 0:
                priority.insert(i, worker)
                i += 1
            else:
                priority.append(worker)
        return priority
