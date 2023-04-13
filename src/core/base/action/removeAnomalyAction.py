from src.core.base.type import ResourceType
from src.core.board.chronossusBoard import ChronossusBoard
from src.core.interface.IAction import IAction
from src.core.interface.IPriority import IPriority
from src.core.util.exception import ActionFailedException


class RemoveAnomalyAction(IAction, IPriority):
    """
    Each time “Remove Anomaly” is selected,
    it discards any 2 Resource cubes. Choose
    Resources it has the most of; if tied, the
    order of priority is:
    Titanium > Gold > Uranium > Neutronium
    1 Neutronium cube is equal to 2 non-Neutronium cubes
    when calculating priority and discarding. Then, if it has the
    Resources to discard, it removes 1 Anomaly. If it doesn’t
    have an Anomaly or the Resources to remove one, it takes
    1 VP instead as usual for Failed Actions
    """

    _board: ChronossusBoard

    def __init__(self, chronossus_board: ChronossusBoard):
        self._board = chronossus_board

    def execute(self) -> None:
        """
        Remove anomaly action
        """
        resources = self.get_priority()
        self._board.resources_pool.remove(resources)
        try:
            self._board.building_pool.remove_anomaly()
        except ActionFailedException:
            for resource in resources:
                self._board.resources_pool.add(resource)
            raise

    def get_priority(self, decrease_priority: list[ResourceType] = None) -> list[ResourceType]:
        """
        Choose Resources it has the most of. If tied, the
        order of priority is:
        Titanium > Gold > Uranium > Neutronium
        1 Neutronium cube is equal to 2 non-Neutronium cubes
        :param decrease_priority: list of resources to decrease priority
        :return: List of resources types ordered by priority
        """
        priority = []
        resource_pool_copy = self._board.resources_pool.get().copy()
        if decrease_priority is not None:
            for resource in decrease_priority:
                resource_pool_copy[resource] -= 1
        resource_pool_copy[ResourceType.NEUTRONIUM] *= 2
        max_resources = self._get_keys_from_value(resource_pool_copy, max(resource_pool_copy.values()))

        if ResourceType.NEUTRONIUM in max_resources and len(max_resources) < 2:
            return [ResourceType.NEUTRONIUM]

        for resource in [ResourceType.TITANIUM, ResourceType.GOLD, ResourceType.URANIUM]:
            if resource in max_resources:
                priority.append(resource)

        if len(priority) < 2 and not decrease_priority:
            priority.extend(self.get_priority([priority[0], ResourceType.NEUTRONIUM]))

        if len(priority) > 2:
            priority = priority[0:2]

        return priority

    def _get_keys_from_value(self, d: dict[ResourceType, int], val: int) -> list[ResourceType]:
        return [k for k, v in d.items() if v == val]
