import pytest

from src.core.base.type import WorkerType
from src.core.board.chronossusBoardComponent.workerPoolComponent import WorkerPoolComponent


class TestWorkerPoolComponent:
    @pytest.mark.parametrize("worker_type", [r for r in WorkerType])
    def test_add(self, worker_type):
        expected_vp = 1
        worker_component = WorkerPoolComponent()
        worker_component.add(worker_type)
        for worker in WorkerType:
            expected = 0
            if worker == worker_type:
                expected = 1
            assert worker_component._pool[worker] == expected
            assert worker_component._score == expected_vp

    def test_add_full_set(self):
        expected = 0
        worker_component = WorkerPoolComponent()
        for worker in WorkerType:
            worker_component.add(worker)
        for worker in WorkerType:
            assert worker_component._pool[worker] == expected

    @pytest.mark.parametrize("workers,expected_vp", [([], 0), ([WorkerType.ADMINISTRATOR], 1),
                                                     ([WorkerType.ADMINISTRATOR, WorkerType.ADMINISTRATOR,
                                                       WorkerType.ENGINEER, WorkerType.SCIENTIST], 4),
                                                     (
                                                             [WorkerType.ADMINISTRATOR, WorkerType.SCIENTIST,
                                                              WorkerType.ENGINEER, WorkerType.GENIUS],
                                                             9),
                                                     (
                                                             [WorkerType.ADMINISTRATOR, WorkerType.SCIENTIST,
                                                              WorkerType.ENGINEER, WorkerType.GENIUS,
                                                              WorkerType.SCIENTIST], 10)])
    def test_get_victory_points(self, workers, expected_vp):
        worker_component = WorkerPoolComponent()
        for worker in workers:
            worker_component.add(worker)
        assert worker_component.get_victory_points() == expected_vp
