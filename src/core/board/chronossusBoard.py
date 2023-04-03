from src.core.board.chronossusBoardComponent.breakthroughPoolComponent import BreakthroughPoolComponent
from src.core.board.chronossusBoardComponent.buildingPoolComponent import BuildingPoolComponent
from src.core.board.chronossusBoardComponent.exosuitPoolComponent import ExosuitPoolComponent
from src.core.board.chronossusBoardComponent.paradoxTrackerComponent import ParadoxTrackerComponent
from src.core.board.chronossusBoardComponent.resourcePoolComponent import ResourcePoolComponent
from src.core.board.chronossusBoardComponent.timeTravelTrackerComponent import TimeTravelTrackerComponent
from src.core.board.chronossusBoardComponent.victoryPointPool import VictoryPointComponent
from src.core.board.chronossusBoardComponent.workerPoolComponent import WorkerPoolComponent


class ChronossusBoard:
    """
    Chronossus board class.
    """

    _actions_tracker = None
    resources_pool: ResourcePoolComponent
    workers_pool: WorkerPoolComponent
    exosuits_pool: ExosuitPoolComponent
    paradox_track: ParadoxTrackerComponent
    time_travel_track: TimeTravelTrackerComponent
    breakthroughs_pool: BreakthroughPoolComponent
    building_pool: BuildingPoolComponent
    victory_points_pool: VictoryPointComponent

    def __init__(self):
        self.building_pool = BuildingPoolComponent()
        self.breakthroughs_pool = BreakthroughPoolComponent()
        self.time_travel_track = TimeTravelTrackerComponent()
        self.paradox_track = ParadoxTrackerComponent()
        self.exosuits_pool = ExosuitPoolComponent()
        self.resources_pool = ResourcePoolComponent()
        self.workers_pool = WorkerPoolComponent()
        self.victory_points_pool = VictoryPointComponent()
