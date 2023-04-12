from src.core.base.type import ActionTileType
from src.core.interface.ITrackerComponent import ITrackerComponent


class ActionSingleTrackerComponent(ITrackerComponent):
    """
    Single tracker of actions
    """

    _tiles: list[ActionTileType]

    def __init__(self, action_tiles: list[ActionTileType]):
        self._tiles = action_tiles
        max_steps = len(action_tiles) - 1
        super().__init__(max_steps)

    def move(self) -> None:
        """
        Move action tracker
        """
        self._step += 1
        if self._step > self.rule_max_steps:
            self._step = 0

    def get_current_action(self) -> ActionTileType:
        """
        Get currently active action
        :return: Actual action
        """
        return self._tiles[self._step]
