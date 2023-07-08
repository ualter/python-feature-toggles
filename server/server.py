from .context import Context
from .request import Request
from .response import Response


def post_request(ctx: Context, req: Request) -> Response:
    func = getattr(__import__('services'), req["action"])
    dataset = func(context=ctx, request=req)
    response = Response(body=dataset)
    return response
