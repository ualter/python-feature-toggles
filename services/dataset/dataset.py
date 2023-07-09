from server import Context
from model import Dataset
from config import Feature
from services import feature_toggle
from .dataset_strategy import StrategyCreateDataset


@feature_toggle(Feature.DATASET_PERMISSIONS_BY_AREA, StrategyCreateDataset)
def create_dataset(context: Context, request: dict) -> Dataset:
    ds = Dataset(owner=context.user, name=request["name"], storage_location=request["storage_location"])
    return ds
