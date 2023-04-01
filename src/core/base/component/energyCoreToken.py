class EnergyCoreToken:
    """
    Model for building tile component
    """

    is_exhausted: bool

    def __init__(self, exhausted=False):
        self.is_exhausted = exhausted
