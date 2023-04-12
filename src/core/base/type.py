from enum import Enum


class BuildingType(Enum):
    """
    Enum class for building types
    """

    POWER_PLANT = "Power plant"
    FACTORY = "Factory"
    LIFE_SUPPORT = "Life support"
    LAB = "Lab"
    SUPER_PROJECT = "Super project"
    ANOMALY = "Anomaly"


class BreakthroughType(Enum):
    """
    Enum class for breakthrough types
    """

    SQUARE = "Square"
    TRIANGLE = "Triangle"
    CIRCLE = "Circle"


class WorkerType(Enum):
    """
    Enum class for worker types
    """

    SCIENTIST = "Scientist"
    ENGINEER = "Engineer"
    ADMINISTRATOR = "Administrator"
    GENIUS = "Genius"


class ResourceType(Enum):
    """
    Enum class for resources types
    """

    NEUTRONIUM = "Neutronium"
    URANIUM = "Uranium"
    GOLD = "Gold"
    TITANIUM = "Titanium"


class ActionTileType(Enum):
    """
    Enum class for action tiles types
    """

    CONSTRUCT_FACTORY = "construct factory"
    CONSTRUCT_LAB = "construct laboratory"
    CONSTRUCT_LIFE_SUPPORT = "construct life support"
    CONSTRUCT_POWER_PLANT = "construct power plant"
    CONSTRUCT_SUPER_PROJECT = "construct super project"
    MINE = "mine"
    RECRUIT_GENIUS_OR_RESEARCH = "recruit genius or do research"
    RECRUIT = "recruit"
    REMOVE_ANOMALY = "remove anomaly"
    RESEARCH = "do research"
    TIME_TRAVEL = "time travel"
    C01A = "reboot"
    C02A = "score"
    C03A = "energy pack"
