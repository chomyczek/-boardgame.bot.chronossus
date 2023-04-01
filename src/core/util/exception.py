class ActionFailedException(Exception):
    """
    Exception for tracking failed actions
    """

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class ParadoxExceededException(Exception):
    """
    Exception for tracking if number of allowed paradox exceeded
    """

    pass


class PassActionsException(Exception):
    """
    Exception for tracking if bot should pass actions
    """

    pass
