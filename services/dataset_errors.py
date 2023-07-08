class DatasetInvalidCreation(Exception):
    """Raise when for some business(controlled) reasons, the creation is not possible"""

    def __init__(self, reason: str, *args: object) -> None:
        self.reason = reason
        super(DatasetInvalidCreation, self).__init__(reason, *args)


