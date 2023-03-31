from src.core.board.chronossusBoard import ChronossusBoard


class Chronossus:
    MAX_WARP_TILES: int = 8
    chronossus_board: ChronossusBoard

    def __init__(self):
        self.chronossus_board = ChronossusBoard()
        self._warp_tiles = self.MAX_WARP_TILES
