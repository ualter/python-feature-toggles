from .user import User


class Dataset:
    def __init__(self, *, owner: User, name: str, storage_location: str) -> None:
        self.owner = owner
        self.name = name
        self.storage_location = storage_location

    def __str__(self):
        me = (
            "Dataset............: "
            + self.name
            + "\nStorage Location...: "
            + self.storage_location
            + "\n"
            + str(self.owner)
        )
        return me
