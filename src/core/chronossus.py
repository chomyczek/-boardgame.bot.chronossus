from src.core.board.chronossusBoard import ChronossusBoard


class Chronossus:
    MAX_WARP_TILES: int = 8
    def __init__(self):
        self.chrono_board: ChronossusBoard = ChronossusBoard()
        self._warp_tiles = self.MAX_WARP_TILES
