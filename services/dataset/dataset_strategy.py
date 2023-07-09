import logging
from model import Dataset
from typing import Callable
from server import Context
from services import Strategy
from abc import abstractmethod
from .dataset_errors import DatasetInvalidCreation


logger = logging.getLogger(__name__)


class StrategyCreateDataset(Strategy):

    """Feature Strategy Decision: here, in case it is Enabled, at this point...
    we define the rule(s) which decides which Strategy Implementation must be choose to be executed"""
    def get_strategy(context: Context, request: dict) -> Strategy:
        return FeaturePermissionAreaCreateDataset()

    @abstractmethod
    def get_strategy_fn_algorithm(context: Context, request: dict) -> Callable:
        pass


class FeaturePermissionAreaCreateDataset(StrategyCreateDataset):
    def get_strategy_fn_algorithm(self, context: Context, request: dict) -> Callable:
        def create_dataset(context: Context, request: dict):
            if context.user.area == "SALES" and request["storage_location"] == "EBS":
                raise DatasetInvalidCreation("SALES are not allow to use EBS")
            else:
                ds = Dataset(owner=context.user, name=request["name"], storage_location=request["storage_location"])
                return ds

        return create_dataset
