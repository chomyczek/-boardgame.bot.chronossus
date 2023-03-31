from src.core.board.chronossusBoardComponent.breakthroughPoolComponent import BreakthroughPoolComponent
from src.core.board.chronossusBoardComponent.buildingsPoolComponent import BuildingPoolComponent


class ChronossusBoard:
    MAX_WARP_TILES: int = 8
    MAX_EXOSUITS: int = 6
    _actions = None
    _resources_pool = None
    _workers_pool = None
    _exosuits_pool = None
    _warp_tiles = None
    _paradox_track = None
    _time_travel_track = None
    _breakthroughs_pool = None
    _buildings_pool: BuildingPoolComponent = None

    def __init__(self):
        self._buildings_pool = BuildingPoolComponent()
        self._breakthroughs_pool = BreakthroughPoolComponent()
