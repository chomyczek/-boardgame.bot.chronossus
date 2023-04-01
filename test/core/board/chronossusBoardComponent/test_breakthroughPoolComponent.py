import pytest

from src.core.base.type import BreakthroughType
from src.core.board.chronossusBoardComponent.breakthroughPoolComponent import BreakthroughPoolComponent
from src.core.util.exception import ActionFailedException


class TestBreakthroughPoolComponent:
    @pytest.mark.parametrize(
        "breakthrough_type", [BreakthroughType.CIRCLE, BreakthroughType.SQUARE, BreakthroughType.TRIANGLE]
    )
    def test_add(self, breakthrough_type):
        breakthrough_component = BreakthroughPoolComponent()
        breakthrough_component.add(breakthrough_type)
        for breakthrough in BreakthroughType:
            expected = 0
            if breakthrough == breakthrough_type:
                expected = 1
            assert breakthrough_component._pool[breakthrough] == expected

    def test_remove_any_each_type_equal(self):
        breakthrough_component = BreakthroughPoolComponent()
        breakthrough_component._pool = {
            BreakthroughType.CIRCLE: 1,
            BreakthroughType.SQUARE: 1,
            BreakthroughType.TRIANGLE: 1,
        }
        breakthrough_component.remove_any()
        assert sum(breakthrough_component._pool.values()) == 2

    def test_remove_any_one_has_more(self):
        breakthrough_component = BreakthroughPoolComponent()
        breakthrough_component._pool = {
            BreakthroughType.CIRCLE: 2,
            BreakthroughType.SQUARE: 1,
            BreakthroughType.TRIANGLE: 1,
        }
        breakthrough_component.remove_any()

        assert breakthrough_component._pool[BreakthroughType.CIRCLE] == 1
        assert breakthrough_component._pool[BreakthroughType.SQUARE] == 1
        assert breakthrough_component._pool[BreakthroughType.TRIANGLE] == 1

    def test_remove_any_empty_pool(self):
        breakthrough_component = BreakthroughPoolComponent()
        with pytest.raises(ActionFailedException) as e:
            breakthrough_component.remove_any()
        assert str(e.value) == "There is no breakthroughs."

    @pytest.mark.parametrize(
        "breakthrough_pool,expected_points",
        [
            ({BreakthroughType.CIRCLE: 1, BreakthroughType.SQUARE: 2, BreakthroughType.TRIANGLE: 3}, 8),
            ({BreakthroughType.CIRCLE: 0, BreakthroughType.SQUARE: 2, BreakthroughType.TRIANGLE: 3}, 5),
        ],
    )
    def test_get_victory_points(self, breakthrough_pool, expected_points):
        breakthrough_component = BreakthroughPoolComponent()
        breakthrough_component._pool = breakthrough_pool
        assert breakthrough_component.get_victory_points() == expected_points
