import pytest

from src.core.base.type import ResourceType
from src.core.board.chronossusBoardComponent.resourcePoolComponent import ResourcePoolComponent
from src.core.util.exception import ActionFailedException


class TestResourcePoolComponent:
    @pytest.mark.parametrize("resource_type", [r for r in ResourceType])
    def test_add(self, resource_type):
        resource_component = ResourcePoolComponent()
        resource_component.add(resource_type)
        for resource in ResourceType:
            expected = 0
            if resource == resource_type:
                expected = 1
            assert resource_component._pool[resource] == expected

    def test_add_full_set(self):
        expected = 0
        resource_component = ResourcePoolComponent()
        for resource in ResourceType:
            resource_component.add(resource)
        for resource in ResourceType:
            assert resource_component._pool[resource] == expected

    @pytest.mark.parametrize("resource_type", [r for r in ResourceType])
    def test_remove_single(self, resource_type):
        expected = 1
        resource_component = ResourcePoolComponent()
        for resource in ResourceType:
            resource_component._pool[resource] = expected
        resource_component.remove([resource_type])
        for resource in ResourceType:
            expected_check = expected
            if resource == resource_type:
                expected_check = 0
            assert resource_component._pool[resource] == expected_check

    @pytest.mark.parametrize("resource_types,after_remove", [([ResourceType.TITANIUM, ResourceType.GOLD], 1), ([ResourceType.NEUTRONIUM, ResourceType.NEUTRONIUM], 0), ([ResourceType.NEUTRONIUM, ResourceType.URANIUM], 1)])
    def test_remove_multiple(self, resource_types, after_remove):
        expected = 2
        resource_component = ResourcePoolComponent()
        for resource in ResourceType:
            resource_component._pool[resource] = expected
        resource_component.remove(resource_types)
        for resource in ResourceType:
            expected_check = expected
            if resource in resource_types:
                expected_check = after_remove
            assert resource_component._pool[resource] == expected_check

    @pytest.mark.parametrize("resource_type", [r for r in ResourceType])
    def test_remove_single_failed(self, resource_type):
        resource_component = ResourcePoolComponent()
        with pytest.raises(ActionFailedException) as e:
            resource_component.remove([resource_type])
        assert str(e.value) == f"There is no {resource_type.value} resources."

    @pytest.mark.parametrize("resource_type,type_info", [([ResourceType.TITANIUM, ResourceType.GOLD],ResourceType.TITANIUM),([ResourceType.GOLD, ResourceType.GOLD],ResourceType.GOLD),([ResourceType.NEUTRONIUM, ResourceType.GOLD, ResourceType.NEUTRONIUM],ResourceType.NEUTRONIUM),([ResourceType.TITANIUM, ResourceType.GOLD,ResourceType.URANIUM, ResourceType.NEUTRONIUM],ResourceType.TITANIUM) ])
    def test_remove_multiple_failed(self, resource_type, type_info):
        resource_component = ResourcePoolComponent()
        with pytest.raises(ActionFailedException) as e:
            resource_component.remove(resource_type)
        assert str(e.value) == f"There is no {type_info.value} resources."

    @pytest.mark.parametrize(
        "resources,expected_vp",
        [
            ([], 0),
            ([ResourceType.TITANIUM], 0),
            ([ResourceType.TITANIUM, ResourceType.TITANIUM, ResourceType.NEUTRONIUM, ResourceType.URANIUM], 0),
            ([ResourceType.TITANIUM, ResourceType.URANIUM, ResourceType.NEUTRONIUM, ResourceType.GOLD], 5),
            (
                [
                    ResourceType.TITANIUM,
                    ResourceType.URANIUM,
                    ResourceType.NEUTRONIUM,
                    ResourceType.GOLD,
                    ResourceType.URANIUM,
                ],
                5,
            ),
        ],
    )
    def test_get_victory_points(self, resources, expected_vp):
        resource_component = ResourcePoolComponent()
        for resource in resources:
            resource_component.add(resource)
        assert resource_component.get_victory_points() == expected_vp
