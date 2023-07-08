class ServiceErrors(Exception):
    """Raise when for some business(controlled) reasons"""

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class DatasetInvalidCreation(ServiceErrors):
    """Raise when for some business(controlled) reasons, the dataset creation is not possible"""

    def __init__(self, reason: str, *args: object) -> None:
        self.reason = reason
        super(DatasetInvalidCreation, self).__init__(reason, *args)
