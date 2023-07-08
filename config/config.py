import yaml
import os


FEATURE_CONFIG_FILE = "./config/features.yml"


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

    def is_storage_permissions_by_area_on(self) -> bool:
        return self.configuration["features"]["storage-permissions-by-area"]["state"]
