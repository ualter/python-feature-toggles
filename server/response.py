from enum import Enum
from services import ServiceErrors


class ResponseStatus(Enum):
    SUCCESS = 200
    FAILED = 500


class Response:
    def __init__(self, *, status: int, body: any, error: ServiceErrors, error_cause: str) -> None:
        self.status = status
        self.body = body
        self.error = error
        self.erro_cause = error_cause
