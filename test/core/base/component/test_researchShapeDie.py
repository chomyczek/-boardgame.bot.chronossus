from src.core.base.component.researchShapeDie import ResearchShapeDie
from src.core.base.type import BreakthroughType


class TestResearchShapeDie:
    def test_roll_use_choices(self, mocker):
        mock_choices = mocker.patch("random.choices")
        ResearchShapeDie().roll()
        assert mock_choices.called

    def test__sides_are_breakthrough_types_only(self):
        sides = ResearchShapeDie()._sides
        assert all(
            side == BreakthroughType.SQUARE or side == BreakthroughType.CIRCLE or side == BreakthroughType.TRIANGLE
            for side in sides
        )
