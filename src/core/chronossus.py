from src.core.board.chronossusBoard import ChronossusBoard


class Chronossus:
    """
    Class for Chronossus bot and its components
    """

    chronossus_board: ChronossusBoard

    def __init__(self):
        self.chronossus_board = ChronossusBoard()

