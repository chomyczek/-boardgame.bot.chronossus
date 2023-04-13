from src.core.base.type import BuildingType
from src.core.board.chronossusBoard import ChronossusBoard
from src.core.interface.IAction import IAction


class ConstructAction(IAction):
    """
    Each of the Chronossus’s Construct Actions is for a specific
    building type (or Superproject). When using the Construct
    Action, the Chronossus always picks the building with the
    higher VP value. If tied, it takes the one in the secondary
    stack. If it already has 3 buildings of the desired type, it takes
    nothing (but it still places an Exosuit to block a Construct
    Action space, and takes 1 VP, as usual, for Failed Actions).
    When Constructing a Superproject, the Chronossus first
    discards a Breakthrough (of any shape or icon; if it has
    multiples, it discards one of whichever it has the most
    of—choose one randomly if tied). Then, it takes the highest VP,
     face-up Superproject from the Present or any past Era (oldest if tied).
    If “Construct Superproject” is rolled and the Chronossus
    does not have a Breakthrough to discard, or it already has 3
    Superprojects, it does nothing (but it still places an Exosuit
    to block a Construct Action space and takes the 1 VP as
    usual for Failed Actions)
    """

    _construction_type: BuildingType
    _board: ChronossusBoard

    def __init__(self, chronossus_board: ChronossusBoard, construction_type: BuildingType):
        self._construction_type = construction_type
        self._board = chronossus_board

    def execute(self, vp: int) -> None:
        """
        Execute construct action
        :param vp: Victory points for taken tile
        """
        self._board.exosuits_pool.place_exosuit()
        if self._construction_type == BuildingType.SUPER_PROJECT:
            self._board.breakthroughs_pool.remove_any()
        self._board.building_pool.add(self._construction_type, vp)
