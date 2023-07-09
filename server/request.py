class Request(dict):
    def __init_subclass__(cls, action: str) -> None:
        return super().__init_subclass__()


def create_dataset_request() -> Request:
    req = Request()
    req["service"] = "dataset"
    req["action"] = "create_dataset"
    return req
