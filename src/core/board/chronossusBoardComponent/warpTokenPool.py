from src.core.util.exception import ActionFailedException


class WarpTokenPool:
    MAX_WARP_TILES: int = 8
    warp_tiles: int

    def __init__(self):
        self.warp_tiles = self.MAX_WARP_TILES

    def add(self):
        if self.warp_tiles == self.MAX_WARP_TILES:
            raise ActionFailedException('There is no warp tokens to remove from Timelines')
        self.warp_tiles += 1
