import enum

from src.core.Interface.IPoolComponent import IPoolComponent
from src.core.Interface.IRewardedComponent import IRewardedComponent
from src.core.base.type import ResourceType
from src.core.util.exception import ActionFailedException


class ResourcePoolComponent(IPoolComponent, IRewardedComponent):

    def add(self, resource: ResourceType):
        super().add(resource)

    def __init__(self):
        super().__init__(ResourceType)

    def remove(self, resource: ResourceType) -> None:
        if self._pool[resource] == 0:
            raise ActionFailedException(f'There is no {resource} resources.')
        self._pool[resource] -= 1

    def get_victory_points(self) -> int:
        """
        Sum of points from pool.
        :return: Collected victory points value from.
        """
        return self._points
