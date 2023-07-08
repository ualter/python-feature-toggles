from .context import Context
from .request import Request
from .response import Response, ResponseStatus
from services import ServiceErrors
from model import Dataset


def post_request(ctx: Context, req: Request) -> Response:
    func = getattr(__import__("services"), req["action"])
    dataset: Dataset = None
    try:
        dataset = func(context=ctx, request=req)
    except ServiceErrors as err:
        return Response(status=ResponseStatus.FAILED, body=dataset, error=err, error_cause=err.__class__.__name__)
    return Response(status=ResponseStatus.SUCCESS, body=dataset, error=None, error_cause=None)
