from server import Context
from model import Dataset
from config import Feature
from .dataset_errors import DatasetInvalidCreation


def create_dataset(context: Context, request: dict) -> Dataset:
    if context.config.is_enable(Feature.DATASET_PERMISSIONS_BY_AREA):
        return _create_dataset_ft_perm_area(context, request)
    else:
        return _create_dataset(context, request)


def _create_dataset(context: Context, request: dict) -> Dataset:
    ds = Dataset(owner=context.user, name=request["name"], storage_location=request["storage_location"])
    return ds


def _create_dataset_ft_perm_area(context: Context, request: dict) -> Dataset:
    if context.user.area == "SALES" and request["storage_location"] == "EBS":
        raise DatasetInvalidCreation("SALES are not allow to use EBS")
    else:
        ds = Dataset(owner=context.user, name=request["name"], storage_location=request["storage_location"])
        return ds
