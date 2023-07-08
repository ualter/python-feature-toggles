from server import Context
from model import Dataset


def create_dataset(context: Context, request: dict) -> Dataset:
    ds = Dataset(owner=context.user, name=request["name"], storage_location=request["storage_location"])
    return ds
