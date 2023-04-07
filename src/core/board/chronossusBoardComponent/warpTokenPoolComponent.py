from src.core.util.exception import ActionFailedException


class WarpTokenPoolComponent:
    """
    resource pool component for chronossus board
    """

    MAX_WARP_TILES: int = 8
    _warp_tiles: int

    def __init__(self):
        self._warp_tiles = self.MAX_WARP_TILES

    def get(self) -> int:
        """
        Get pool from component
        :return: number of warp tokens
        """
        return self._warp_tiles

    def add(self) -> None:
        """
        Add token to pool
        """
        if self._warp_tiles == self.MAX_WARP_TILES:
            raise ActionFailedException("There is no warp tokens to remove from the Timelines.")
        self._warp_tiles += 1

    def remove(self) -> None:
        """
        Remove token from pool
        """
        if self._warp_tiles == 0:
            raise ActionFailedException("All warp tokens was already placed on the Timelines.")
        self._warp_tiles -= 1
