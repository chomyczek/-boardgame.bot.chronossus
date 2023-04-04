from src.core.base.action.failedAction import FailedAction
from src.core.base.type import ResourceType
from src.core.board.chronossusBoard import ChronossusBoard
from src.core.interface.IAction import IAction
from src.core.interface.IPriority import IPriority
from src.core.util.exception import ActionFailedException


class RemoveAnomalyAction(IAction, IPriority):
    _board: ChronossusBoard
    _failedAction: FailedAction

    def __init__(self, chronossus_board: ChronossusBoard):
        self._board = chronossus_board
        self._failedAction = FailedAction(chronossus_board)

    def execute(self) -> None:
        resources = self.get_priority()
        try:
            self._board.resources_pool.remove(resources)
        except ActionFailedException:
            self._failedAction.execute()

    def get_priority(self, decrease_priority: list[ResourceType] = None) -> list[ResourceType]:
        priority = []
        resource_pool_copy = self._board.resources_pool.get().copy()
        if decrease_priority is not None:
            for resource in decrease_priority:
                resource_pool_copy[resource] -= 1
        resource_pool_copy[ResourceType.NEUTRONIUM] *= 2
        max_resources = self._get_keys_from_value(resource_pool_copy, max(resource_pool_copy.values()))

        if ResourceType.NEUTRONIUM in max_resources and len(max_resources) <= 2:
            return [ResourceType.NEUTRONIUM]

        for resource in [ResourceType.TITANIUM, ResourceType.GOLD, ResourceType.URANIUM]:
            if resource in max_resources:
                priority.append(resource)

        if len(priority) < 2:
            priority.append(self.get_priority([priority[0], ResourceType.NEUTRONIUM]))
            if ResourceType.NEUTRONIUM in priority:
                return [ResourceType.NEUTRONIUM]

        if len(priority) > 2:
            priority = priority[0:2]

        return priority

    def _get_keys_from_value(self, d: dict[ResourceType, int], val: int) -> list[ResourceType]:
        return [k for k, v in d.items() if v == val]
