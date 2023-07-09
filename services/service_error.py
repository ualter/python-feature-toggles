class ServiceErrors(Exception):
    """Raise when for some business(controlled) reasons"""

    def __init__(self, *args: object) -> None:
        super().__init__(*args)
