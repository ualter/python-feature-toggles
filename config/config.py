import yaml
import os
from enum import Enum


FEATURE_CONFIG_FILE = "./config/features.yml"


class Feature(Enum):
    DATASET_PERMISSIONS_BY_AREA = 1


class ConfigException(Exception):
    def __init__(self, message: str, *args: object) -> None:
        self.message = message
        super(ConfigException, self).__init__(message, *args)


class Config:
    def __init__(self) -> None:
        file_path = os.path.join(FEATURE_CONFIG_FILE)
        if os.path.exists(file_path):
            with open(file_path) as f:
                self.configuration = yaml.load(f, Loader=yaml.FullLoader)
        else:
            raise ConfigException(message="File " + file_path + "not found")

    def is_enable(self, feature: Feature) -> bool:
        features = self.configuration["features"]

        match feature:
            case Feature.DATASET_PERMISSIONS_BY_AREA:
                return features["dataset-permissions-by-area"]["state"]
            case _:
                return False
