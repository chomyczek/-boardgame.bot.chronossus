import random

from src.core.base.type import BreakthroughType
from src.core.interface.IDie import IDie


class ResearchShapeDie(IDie):
    """
    Class with Breakthrough shapes for research action
    """

    _sides: list[BreakthroughType] = [
        BreakthroughType.SQUARE,
        BreakthroughType.CIRCLE,
        BreakthroughType.TRIANGLE,
        BreakthroughType.SQUARE,
        BreakthroughType.CIRCLE,
        BreakthroughType.TRIANGLE,
    ]

    def roll(self) -> BreakthroughType:
        """
        Roll the dice
        :return: Breakthrough as a result of rolled die
        """
        return random.choices(self._sides)[0]
