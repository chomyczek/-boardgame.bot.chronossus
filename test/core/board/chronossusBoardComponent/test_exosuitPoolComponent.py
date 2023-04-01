import itertools

import pytest

from src.core.board.chronossusBoardComponent.exosuitPoolComponent import ExosuitPoolComponent
from src.core.util.exception import PassActionsException


class TestExosuitPoolComponent:

    def test_trigger_impact(self):
        rule_max_exosuits_before_impact = 6
        rule_guaranteed_exosuits_before_impact = 3
        rule_max_exosuits_after_impact = 4
        rule_guaranteed_exosuits_after_impact = 2
        exosuit_pool_component = ExosuitPoolComponent()
        assert exosuit_pool_component.rule_max_exosuits == rule_max_exosuits_before_impact
        assert exosuit_pool_component.rule_guaranteed_exosuits == rule_guaranteed_exosuits_before_impact

        exosuit_pool_component.trigger_impact()

        assert exosuit_pool_component.rule_max_exosuits == rule_max_exosuits_after_impact
        assert exosuit_pool_component.rule_guaranteed_exosuits == rule_guaranteed_exosuits_after_impact

    def test_add_energy_core(self):
        exosuit_pool_component = ExosuitPoolComponent()
        starting_core_pool = len([c.is_exhausted for c in exosuit_pool_component._energy_cores_pool])
        exosuit_pool_component.add_energy_core()
        post_action_core_pool = len([c.is_exhausted for c in exosuit_pool_component._energy_cores_pool])
        assert post_action_core_pool == starting_core_pool + 1

    def test_add_exhausted_energy_core(self):
        exosuit_pool_component = ExosuitPoolComponent()
        starting_core_pool = len([not c.is_exhausted for c in exosuit_pool_component._energy_cores_pool])
        exosuit_pool_component.add_exhausted_energy_core()
        post_action_core_pool = len([not c.is_exhausted for c in exosuit_pool_component._energy_cores_pool])
        assert post_action_core_pool == starting_core_pool + 1

    def test_place_exosuit(self):
        powered_up_exosuits = 5
        exosuit_pool_component = ExosuitPoolComponent()
        exosuit_pool_component._powered_up_exosuits = powered_up_exosuits
        exosuit_pool_component.place_exosuit()
        assert exosuit_pool_component._powered_up_exosuits == powered_up_exosuits - 1

    def test_place_exosuit_empty_powered_up_exosuits_pool(self):
        exosuit_pool_component = ExosuitPoolComponent()
        with pytest.raises(PassActionsException):
            exosuit_pool_component.place_exosuit()

    @pytest.mark.parametrize("trigger_impact", [True, False])
    def test_power_up_exosuits_only_normal_cores(self, trigger_impact, mocker):
        mock_shuffle = mocker.patch('src.core.board.chronossusBoardComponent.exosuitPoolComponent.shuffle')
        exosuit_pool_component = ExosuitPoolComponent()
        exosuit_pool_component._energy_cores_pool = []
        for i in range(10):
            exosuit_pool_component.add_energy_core()
        if trigger_impact:
            exosuit_pool_component.trigger_impact()
        exosuit_pool_component.power_up_exosuits()
        assert exosuit_pool_component._powered_up_exosuits == exosuit_pool_component.rule_max_exosuits
        assert mock_shuffle.called

    @pytest.mark.parametrize("trigger_impact,exhausted_count", list(
        itertools.product([True, False], range(1, ExosuitPoolComponent.rule_num_of_draws + 1))))
    def test_power_up_exosuits_exhausted_drawn(self, trigger_impact, exhausted_count, mocker):
        exhausted_not_drawn = 2
        mocker.patch('src.core.board.chronossusBoardComponent.exosuitPoolComponent.shuffle', )
        exosuit_pool_component = ExosuitPoolComponent()
        exosuit_pool_component._energy_cores_pool = []
        for i in range(exhausted_not_drawn):
            exosuit_pool_component.add_exhausted_energy_core()
        for i in range(5):
            exosuit_pool_component.add_energy_core()
        for i in range(exhausted_count):
            exosuit_pool_component.add_exhausted_energy_core()
        if trigger_impact:
            exosuit_pool_component.trigger_impact()
        exosuit_pool_component.power_up_exosuits()

        exhausted_left = len([c for c in exosuit_pool_component._energy_cores_pool if c.is_exhausted])
        expected_powered_up_exosuits = min(
            exosuit_pool_component.rule_num_of_draws + exosuit_pool_component.rule_guaranteed_exosuits - exhausted_count,
            exosuit_pool_component.rule_max_exosuits)
        assert exosuit_pool_component._powered_up_exosuits == expected_powered_up_exosuits
        assert exhausted_left == exhausted_not_drawn + 1

    @pytest.mark.parametrize("trigger_impact,core_pool_count",
                             list(itertools.product([True, False], range(ExosuitPoolComponent.rule_num_of_draws))))
    def test_power_up_exosuits_not_enough_tokens(self, trigger_impact, core_pool_count):
        exosuit_pool_component = ExosuitPoolComponent()
        exosuit_pool_component._energy_cores_pool = []
        for i in range(core_pool_count):
            exosuit_pool_component.add_energy_core()
        if trigger_impact:
            exosuit_pool_component.trigger_impact()
        exosuit_pool_component.power_up_exosuits()
        assert exosuit_pool_component._powered_up_exosuits == \
               exosuit_pool_component.rule_guaranteed_exosuits + core_pool_count
