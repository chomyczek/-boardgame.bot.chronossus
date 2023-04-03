import random

from src.core.base.type import BreakthroughType
from src.core.interface.IDie import IDie


class ResearchShapeDie(IDie):
    _sides: list[BreakthroughType] = [BreakthroughType.SQUARE, BreakthroughType.CIRCLE, BreakthroughType.TRIANGLE,
                                      BreakthroughType.SQUARE, BreakthroughType.CIRCLE, BreakthroughType.TRIANGLE]

    def roll(self):
        return random.choices(self._sides)
