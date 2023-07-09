import logging
from config import Feature


logger = logging.getLogger(__name__)


def feature_toggle(feature: Feature, feature_func):
    def decorator(func):
        def wrapper(*args, **kwargs):
            context = kwargs["context"]
            if context.config.is_enable(feature):
                logger.info("Feature " + feature.name + " is ENABLED")
                return feature_func(*args, **kwargs)
            else:
                logger.info("Feature " + feature.name + " is DISABLED")
                return func(*args, **kwargs)

        return wrapper

    return decorator
