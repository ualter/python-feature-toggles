import logging
from server import Context
from model import Dataset
from config import Feature
from services import feature_toggle
from .dataset_errors import DatasetInvalidCreation

logger = logging.getLogger(__name__)


def _create_dataset_ft_perm_area(context: Context, request: dict) -> Dataset:
    logging.info(f"Using ALTERNATIVE route path, feature toggle {Feature.DATASET_PERMISSIONS_BY_AREA.name} is ON")
    if context.user.area == "SALES" and request["storage_location"] == "EBS":
        raise DatasetInvalidCreation("SALES are not allow to use EBS")
    else:
        ds = Dataset(owner=context.user, name=request["name"], storage_location=request["storage_location"])
        return ds


@feature_toggle(Feature.DATASET_PERMISSIONS_BY_AREA, _create_dataset_ft_perm_area)
def create_dataset(context: Context, request: dict) -> Dataset:
    logging.info(f"Using REGULAR route path, feature toggle {Feature.DATASET_PERMISSIONS_BY_AREA.name} is OFF")
    ds = Dataset(owner=context.user, name=request["name"], storage_location=request["storage_location"])
    return ds
