from typing import Any
from .context import Context
from .request import Request
from .response import Response, ResponseStatus
from services import ServiceErrors
import importlib.util


def do_post_request(ctx: Context, req: Request) -> Response:
    service_module = importlib.import_module("services." + req["service"])
    func = getattr(service_module, req["action"])
    payload: Any = None
    try:
        payload = func(context=ctx, request=req)
    except ServiceErrors as err:
        return Response(status=ResponseStatus.FAILED, body=payload, error=err, error_cause=err.__class__.__name__)
    return Response(status=ResponseStatus.SUCCESS, body=payload, error=None, error_cause=None)
