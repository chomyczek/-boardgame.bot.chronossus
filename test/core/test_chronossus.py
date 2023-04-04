from src.core.chronossus import Chronossus


class TestChronossus:
    def test_init(self):
        chronossus = Chronossus()
        assert chronossus.chronossus_board is not None
