class DatasetInvalidCreation(Exception):
    """Raise when for some business(controlled) reasons, the creation is not possible"""

    def __init__(self, *args: object) -> None:
        super().__init__(*args)
