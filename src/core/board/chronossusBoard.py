from src.core.board.chronossusBoardComponent.actionTrackerComponent import ActionTrackerComponent
from src.core.board.chronossusBoardComponent.breakthroughPoolComponent import BreakthroughEnumPoolComponent
from src.core.board.chronossusBoardComponent.buildingPoolComponent import BuildingPoolComponent
from src.core.board.chronossusBoardComponent.exosuitPoolComponent import ExosuitPoolComponent
from src.core.board.chronossusBoardComponent.paradoxTrackerComponent import ParadoxTrackerComponent
from src.core.board.chronossusBoardComponent.resourcePoolComponent import ResourceEnumPoolComponent
from src.core.board.chronossusBoardComponent.timeTravelTrackerComponent import TimeTravelTrackerComponent
from src.core.board.chronossusBoardComponent.victoryPointPoolComponent import VictoryPointComponent
from src.core.board.chronossusBoardComponent.warpTokenPoolComponent import WarpTokenPoolComponent
from src.core.board.chronossusBoardComponent.workerPoolComponent import WorkerEnumPoolComponent


class ChronossusBoard:
    """
    Chronossus board class.
    """

    actions_tracker: ActionTrackerComponent
    resources_pool: ResourceEnumPoolComponent
    workers_pool: WorkerEnumPoolComponent
    exosuits_pool: ExosuitPoolComponent
    paradox_track: ParadoxTrackerComponent
    time_travel_track: TimeTravelTrackerComponent
    breakthroughs_pool: BreakthroughEnumPoolComponent
    building_pool: BuildingPoolComponent
    victory_points_pool: VictoryPointComponent
    warp_token_pool: WarpTokenPoolComponent

    def __init__(self):
        self.building_pool = BuildingPoolComponent()
        self.breakthroughs_pool = BreakthroughEnumPoolComponent()
        self.time_travel_track = TimeTravelTrackerComponent()
        self.paradox_track = ParadoxTrackerComponent()
        self.exosuits_pool = ExosuitPoolComponent()
        self.resources_pool = ResourceEnumPoolComponent()
        self.workers_pool = WorkerEnumPoolComponent()
        self.victory_points_pool = VictoryPointComponent()
        self.warp_token_pool = WarpTokenPoolComponent()
        self.actions_tracker = ActionTrackerComponent()
