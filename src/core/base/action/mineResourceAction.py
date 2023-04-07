from src.core.base.action.failedAction import FailedAction
from src.core.base.type import ResourceType
from src.core.board.chronossusBoard import ChronossusBoard
from src.core.interface.IAction import IAction
from src.core.interface.IPriority import IPriority


class MineResourceAction(IAction, IPriority):
    """
    When taking the Mine Resource Action, the Chronossus
    determines which 2 Resources it wants the most.
    • It prioritizes Resources it does not have.
    • If tied, it chooses based on the following priority:
    Neutronium > Uranium > Gold > Titanium
    Then, it takes the Mine Resource Action space from which
    these 2 Resources can be gained. If multiple possibilities
    are available, it selects the topmost one.
    Once it has at least one of all 4 Resource types, it discards
    one of each and gains 5 VPs.
    """

    _board: ChronossusBoard
    _failedAction: FailedAction

    def __init__(self, chronossus_board: ChronossusBoard):
        self._board = chronossus_board
        self._failedAction = FailedAction(chronossus_board)

    def get_priority(self) -> list[ResourceType]:
        """
        It prioritizes Resources it does not have.
        If tied, it chooses based on the following priority:
        Neutronium > Uranium > Gold > Titanium
        :return: list of resources ordered by priority
        """

        pool = self._board.resources_pool.get()
        general_priority = [ResourceType.NEUTRONIUM, ResourceType.URANIUM, ResourceType.GOLD, ResourceType.TITANIUM]
        priority = sorted(pool, key=lambda k: (pool[k], general_priority.index(k)))
        return priority

    def execute(self, resource_type_one: ResourceType, resource_type_two: ResourceType) -> None:
        """
        Execute main resource action
        :param resource_type_one: First selected resource
        :param resource_type_two: Second selected resource
        """
        self._board.exosuits_pool.place_exosuit()
        if resource_type_one:
            self._board.resources_pool.add(resource_type_one)
        if resource_type_two:
            self._board.resources_pool.add(resource_type_two)
