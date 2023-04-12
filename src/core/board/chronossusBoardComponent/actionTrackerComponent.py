from __future__ import annotations

from src.core.base.type import ActionTileType
from src.core.board.chronossusBoardComponent.singleActionTrackerComponent import ActionSingleTrackerComponent


class ActionTrackerComponent:
    """
    Action tracker component of Chronossus board
    """

    _trackers: dict[int, ActionSingleTrackerComponent]

    def __init__(self):
        self._trackers = {
            2: self._get_2nd_tracker_component(),
            3: self._get_3rd_tracker_component(),
            4: self._get_4th_tracker_component(),
            5: self._get_5th_tracker_component(),
        }

    @staticmethod
    def _get_2nd_tracker_component() -> ActionSingleTrackerComponent:
        actions = [
            ActionTileType.CONSTRUCT_POWER_PLANT,
            ActionTileType.MINE,
            ActionTileType.C01A,
            ActionTileType.RECRUIT,
            ActionTileType.RESEARCH
        ]
        return ActionSingleTrackerComponent(actions)

    @staticmethod
    def _get_3rd_tracker_component() -> ActionSingleTrackerComponent:
        actions = [
            ActionTileType.CONSTRUCT_LIFE_SUPPORT,
            ActionTileType.TIME_TRAVEL,
            ActionTileType.C02A,
            ActionTileType.CONSTRUCT_SUPER_PROJECT,
            ActionTileType.REMOVE_ANOMALY
        ]
        return ActionSingleTrackerComponent(actions)

    @staticmethod
    def _get_4th_tracker_component() -> ActionSingleTrackerComponent:
        actions = [
            ActionTileType.CONSTRUCT_FACTORY,
            ActionTileType.C01A,
            ActionTileType.MINE,
            ActionTileType.CONSTRUCT_LAB,
            ActionTileType.RECRUIT_GENIUS_OR_RESEARCH
        ]
        return ActionSingleTrackerComponent(actions)

    @staticmethod
    def _get_5th_tracker_component() -> ActionSingleTrackerComponent:
        actions = [
            ActionTileType.RECRUIT,
            ActionTileType.RESEARCH,
            ActionTileType.CONSTRUCT_POWER_PLANT,
            ActionTileType.C03A,
        ]
        return ActionSingleTrackerComponent(actions)

    def get_action(
            self,
            tracker: int
    ) -> ActionTileType:
        """
        Get current action type of provided tracker
        :param tracker: Type of action tracker
        :return: Current action enum
        """

        return self._trackers[tracker].get_current_action()

    def move_action(
            self,
            tracker: int
    ) -> None:
        """
        Move action on provided tracker
        :param tracker: Type of action tracker
        """
        self._trackers[tracker].move()
