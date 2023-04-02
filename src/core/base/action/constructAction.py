from src.core.base.action.failedAction import FailedAction
from src.core.base.type import BuildingType
from src.core.board.chronossusBoard import ChronossusBoard
from src.core.interface.IAction import IAction
from src.core.util.exception import ActionFailedException


class ConstructAction(IAction):

    _construction_type: BuildingType
    _board: ChronossusBoard
    _failedAction: FailedAction

    def __init__(self, chronossus_board: ChronossusBoard, construction_type: BuildingType):
        self._construction_type = construction_type
        self._board = chronossus_board
        self._failedAction = FailedAction(chronossus_board)

    def execute(self, vp: int) -> None:
        try:
            self._board.exosuits_pool.place_exosuit()
            if self._construction_type == BuildingType.SUPER_PROJECT:
                self._board.breakthroughs_pool.remove_any()
            self._board.building_pool.add(self._construction_type, vp)
        except ActionFailedException:
            self._failedAction.execute()
