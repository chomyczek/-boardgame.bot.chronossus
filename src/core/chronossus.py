from src.core.board.chronossusBoard import ChronossusBoard


class Chronossus:
    MAX_WARP_TILES: int = 8
    chronossus_board: ChronossusBoard
    warp_tiles: int

    def __init__(self):
        self.chronossus_board = ChronossusBoard()
        self.warp_tiles = self.MAX_WARP_TILES
