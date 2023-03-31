from enum import Enum


class BuildingType(Enum):
    POWER_PLANT = 'Power plant'
    FACTORY = 'Factory'
    LIFE_SUPPORT = 'Life support'
    LAB = 'Lab'
    SUPER_PROJECT = 'Super project'
    ANOMALY = 'Anomaly'


class BreakthroughType(Enum):
    SQUARE = 'Square'
    TRIANGLE = 'Triangle'
    CIRCLE = 'Circle'


class WorkerType(Enum):
    SCIENTIST = 'Scientist'
    ENGINEER = 'Engineer'
    ADMINISTRATOR = 'Administrator'
    GENIUS = 'Genius'


class ResourceType(Enum):
    NEUTRONIUM = 'Neutronium'
    URANIUM = 'Uranium'
    GOLD = 'Gold'
    TITANIUM = 'Titanium'
