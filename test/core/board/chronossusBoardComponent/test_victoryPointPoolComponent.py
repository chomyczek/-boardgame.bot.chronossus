import pytest

from src.core.board.chronossusBoardComponent.victoryPointPoolComponent import VictoryPointComponent


class TestVictoryPointComponent:

    @pytest.mark.parametrize("vps,score", [([1],1),([2,5,88],95)])
    def test_add(self, vps, score):
        vp_component = VictoryPointComponent()
        for vp in vps:
            vp_component.add(vp)
        assert vp_component._score == score

    @pytest.mark.parametrize("vps,score", [([2],2),([2,5,88,5],100)])
    def test_get_victory_points(self, vps, score):
        vp_component = VictoryPointComponent()
        for vp in vps:
            vp_component.add(vp)
        assert vp_component.get_victory_points() == score