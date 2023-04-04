import pytest

from src.core.board.chronossusBoardComponent.warpTokenPoolComponent import WarpTokenPoolComponent
from src.core.util.exception import ActionFailedException


class TestWarpTokenPoolComponent:
    @pytest.mark.parametrize("count", range(1,8))
    def test_add(self, count: int):
        warp_pool = WarpTokenPoolComponent()
        warp_pool._warp_tiles = 0
        for i in range(count):
            warp_pool.add()

        assert warp_pool._warp_tiles == count

    @pytest.mark.parametrize("count", [9,15,57,255])
    def test_add_action_failed(self, count):
        warp_pool = WarpTokenPoolComponent()
        warp_pool._warp_tiles = 0
        with pytest.raises(ActionFailedException) as e:
            for i in range(count):
                warp_pool.add()
        assert str(e.value) == f"There is no warp tokens to remove from the Timelines."


    @pytest.mark.parametrize("count", range(1,8))
    def test_remove(self, count: int):
        warp_pool = WarpTokenPoolComponent()
        for i in range(count):
            warp_pool.remove()

        assert warp_pool._warp_tiles == 8 - count

    @pytest.mark.parametrize("count", [9,15,57,255])
    def test_remove_action_failed(self, count):
        warp_pool = WarpTokenPoolComponent()
        with pytest.raises(ActionFailedException) as e:
            for i in range(count):
                warp_pool.remove()
        assert str(e.value) == f"All warp tokens should be already placed on the Timelines."

    def test_get(self):
        warp_pool = WarpTokenPoolComponent()
        assert warp_pool.get() == 8
