class ActionFailedException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class ParadoxExceededException(Exception):
    pass


class PassActionsException(Exception):
    pass
