import logging
import importlib
from config import Feature
from abc import ABC


logger = logging.getLogger(__name__)


def feature_toggle(feature: Feature, featureStrategy: ABC):
    def decorator(func):
        def wrapper(*args, **kwargs):
            context = kwargs["context"]
            request = kwargs["request"]

            """Feature Toggle Decision: this point we check if the feature is Enabled"""
            if context.config.is_enable(feature):
                logger.debug("Feature " + feature.name + " is ENABLED")
                featureStrategyImpl = featureStrategy.get_strategy(context, request)
                fn = featureStrategyImpl.get_strategy_fn_algorithm(context, request)
                return fn(*args, **kwargs)
            else:
                logger.debug("Feature " + feature.name + " is DISABLED")
                return func(*args, **kwargs)

        return wrapper

    return decorator
