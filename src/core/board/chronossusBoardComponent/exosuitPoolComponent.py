from random import shuffle

from src.core.base.component.energyCoreToken import EnergyCoreToken
from src.core.util.exception import PassActionsException


class ExosuitPoolComponent:
    """
    Exosuit pool component for chronossus board
    """

    rule_num_of_draws = 3
    rule_max_exosuits: int
    rule_guaranteed_exosuits: int
    _energy_cores_pool: list[EnergyCoreToken]
    _powered_up_exosuits: int

    def __init__(self):
        self.rule_max_exosuits = 6
        self.rule_guaranteed_exosuits = 3
        self._powered_up_exosuits = 0
        self._energy_cores_pool = []
        # Fill it with 5 Energy Core tokens and 5 Exhausted Energy Core tokens
        for i in range(5):
            self.add_energy_core()
            self.add_exhausted_energy_core()

    def trigger_impact(self) -> None:
        """
        Adjust rules for exosuits after impact
        """
        self.rule_max_exosuits = 4
        self.rule_guaranteed_exosuits = 2

    def add_energy_core(self) -> None:
        """
        Add one standard energy core to pool
        """
        self._energy_cores_pool.append(EnergyCoreToken())

    def add_exhausted_energy_core(self) -> None:
        """
        Add one exhausted energy core to pool
        """
        self._energy_cores_pool.append(EnergyCoreToken(True))

    def place_exosuit(self) -> None:
        """
        Remove one of powered up exosuits
        """
        if self._powered_up_exosuits == 0:
            raise PassActionsException()
        self._powered_up_exosuits -= 1

    def power_up_exosuits(self) -> None:
        """
        In the Power up Phase, determine the number of Exosuits to be powered up. Draw 3 tokens from its Energy Pool.
        Before the Impact, the Chronossus powers up 3+X Exosuits, where X equals the (non-exhausted) Energy Cores drawn
        (maximum of 6 Exosuits). After the Impact, the Chronossus powers up 2+X Exosuits, where X equals the
        (non-exhausted) Energy Cores drawn (maximum of 4 Exosuits). Afterwards, return 1 drawn Exhausted Energy Core to
        the Energy Pool, and remove the other drawn tokens from the game. If there are less than 3 tokens left in the
        Energy Pool, draw as many as can be drawn.
        """
        drawn = self.rule_guaranteed_exosuits + self._draw_core_from_pool()
        self._powered_up_exosuits = min(drawn, self.rule_max_exosuits)

    def _draw_core_from_pool(self) -> int:
        if not any(self._energy_cores_pool):
            return 0
        num_of_draws = min(self.rule_num_of_draws, len(self._energy_cores_pool))
        shuffle(self._energy_cores_pool)
        exhausted_core_drawn = 0
        for i in range(num_of_draws):
            core = self._energy_cores_pool.pop()
            if core.is_exhausted:
                exhausted_core_drawn += 1
        # Afterwards, return 1 drawn Exhausted Energy Core to the Energy Pool
        if exhausted_core_drawn >= 1:
            self.add_exhausted_energy_core()
        return num_of_draws - exhausted_core_drawn
