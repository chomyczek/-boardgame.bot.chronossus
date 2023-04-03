from src.core.base.action.failedAction import FailedAction
from src.core.base.type import ResourceType
from src.core.board.chronossusBoard import ChronossusBoard
from src.core.interface.IAction import IAction
from src.core.interface.IPriority import IPriority
from src.core.util.exception import ActionFailedException


class MineResourceAction(IAction, IPriority):
    _board: ChronossusBoard
    _failedAction: FailedAction

    def __init__(self, chronossus_board: ChronossusBoard):
        self._board = chronossus_board
        self._failedAction = FailedAction(chronossus_board)

    def get_priority(self) -> list[ResourceType]:
        priority = []
        pool = self._board.resources_pool.get()
        i = 0
        for resource in [ResourceType.NEUTRONIUM, ResourceType.URANIUM, ResourceType.GOLD, ResourceType.TITANIUM]:
            if pool[resource] == 0:
                priority.insert(i, resource)
                i += 1
            else:
                priority.append(resource)
        return priority

    def execute(self, resource_type_one: ResourceType, resource_type_two: ResourceType) -> None:
        try:
            self._board.exosuits_pool.place_exosuit()
            if resource_type_one:
                self._board.resources_pool.add(resource_type_one)
            if resource_type_two:
                self._board.resources_pool.add(resource_type_two)
        except ActionFailedException:
            self._failedAction.execute()
