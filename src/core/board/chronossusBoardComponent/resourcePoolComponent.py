from src.core.base.type import ResourceType
from src.core.interface.IEnumPoolComponent import IEnumPoolComponent
from src.core.interface.IRewardedComponent import IRewardedComponent
from src.core.util.exception import ActionFailedException


class ResourceEnumPoolComponent(IEnumPoolComponent, IRewardedComponent):
    """
    resource pool component for chronossus board
    """

    def add(self, resource: ResourceType):
        super().add(resource)
        super().check_for_completed_set()

    def __init__(self):
        super().__init__(ResourceType)

    def remove(self, resources: list[ResourceType]) -> None:
        """
        Remove one resource of provided type from the pool
        :param resources: Resource type to remove
        """
        for resource in resources:
            if self._pool[resource] == 0:
                raise ActionFailedException(f"There is no {resource.value} resources.")
        for resource in resources:
            self._pool[resource] -= 1

    def get_victory_points(self) -> int:
        """
        Sum of points from pool.
        :return: Collected victory points value from.
        """
        return self._score

    def get(self) -> dict[ResourceType, int]:
        return self._pool
