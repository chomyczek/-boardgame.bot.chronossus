from src.core.base.action.failedAction import FailedAction
from src.core.base.type import ResourceType
from src.core.board.chronossusBoard import ChronossusBoard
from src.core.interface.IAction import IAction
from src.core.interface.IPriority import IPriority


class MineResourceAction(IAction, IPriority):
    _board: ChronossusBoard
    _failedAction: FailedAction

    def __init__(self, chronossus_board: ChronossusBoard):
        self._board = chronossus_board
        self._failedAction = FailedAction(chronossus_board)

    def get_priority(self) -> list[ResourceType]:
        pool = self._board.resources_pool.get()
        general_priority = [ResourceType.NEUTRONIUM, ResourceType.URANIUM, ResourceType.GOLD, ResourceType.TITANIUM]
        priority = sorted(pool, key=lambda k: (pool[k], general_priority.index(k)))
        return priority

    def execute(self, resource_type_one: ResourceType, resource_type_two: ResourceType) -> None:
        self._board.exosuits_pool.place_exosuit()
        if resource_type_one:
            self._board.resources_pool.add(resource_type_one)
        if resource_type_two:
            self._board.resources_pool.add(resource_type_two)
