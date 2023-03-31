from src.core.board.chronossusBoardComponent.resourcePoolComponent import ResourcePoolComponent
from src.core.board.chronossusBoardComponent.workerPoolComponent import WorkerPoolComponent
from src.core.board.chronossusBoardComponent.breakthroughPoolComponent import BreakthroughPoolComponent
from src.core.board.chronossusBoardComponent.buildingPoolComponent import BuildingPoolComponent
from src.core.board.chronossusBoardComponent.exosuitPoolComponent import ExosuitPoolComponent
from src.core.board.chronossusBoardComponent.paradoxTrackerComponent import ParadoxTrackerComponent
from src.core.board.chronossusBoardComponent.timeTravelTrackerComponent import TimeTravelTrackerComponent


class ChronossusBoard:
    _actions = None
    _resources_pool: ResourcePoolComponent
    _workers_pool: WorkerPoolComponent
    _exosuits_pool: ExosuitPoolComponent
    _paradox_track: ParadoxTrackerComponent
    _time_travel_track: TimeTravelTrackerComponent
    _breakthroughs_pool: BreakthroughPoolComponent
    _building_pool: BuildingPoolComponent

    def __init__(self):
        self._building_pool = BuildingPoolComponent()
        self._breakthroughs_pool = BreakthroughPoolComponent()
        self._time_travel_track = TimeTravelTrackerComponent()
        self._paradox_track = ParadoxTrackerComponent()
        self._exosuits_pool = ExosuitPoolComponent()
        self._resources_pool = ResourcePoolComponent()
