from src.core.util.exception import ActionFailedException


class WarpTokenPoolComponent:
    MAX_WARP_TILES: int = 8
    _warp_tiles: int

    def __init__(self):
        self._warp_tiles = self.MAX_WARP_TILES

    def get(self) -> int:
        return self._warp_tiles

    def add(self) -> None:
        if self._warp_tiles == self.MAX_WARP_TILES:
            raise ActionFailedException("There is no warp tokens to remove from the Timelines.")
        self._warp_tiles += 1

    def remove(self) -> None:
        if self._warp_tiles == 0:
            raise ActionFailedException("All warp tokens was already placed on the Timelines.")
        self._warp_tiles -= 1
