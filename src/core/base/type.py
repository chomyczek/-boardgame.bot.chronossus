from enum import Enum


class BuildingType(Enum):
    POWER_PLANT = 'Power plant'
    FACTORY = 'Factory'
    LIFE_SUPPORT = 'Life support'
    LAB = 'Lab'
    SUPER_PROJECT = 'Super project'
    ANOMALY = 'Anomaly'


class BreakthroughsType(Enum):
    SQUARE = 'Square'
    TRIANGLE = 'Triangle'
    CIRCLE = 'Circle'
