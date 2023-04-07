from src.core.interface.IAction import IAction  # pragma: no cover - This action does nothing


class RebootAction(IAction):  # pragma: no cover - This action does nothing
    """
    Each time “Reboot” is selected, the
    Chronossus simply does nothing. This
    does not count as a Failed Action, and it
    does not receive 1 VP
    """

    def execute(self) -> None:
        pass
