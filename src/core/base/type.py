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
