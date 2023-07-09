from db import get_user
from model import User
from typing import Any
from config import Config, Feature
from server import Context, Request, ResponseStatus, create_dataset_request, do_post_request


def post_user_request(user: User, req: Request) -> Any:
    ctx = Context(user=user)
    response = do_post_request(ctx, req)
    if response.status == ResponseStatus.FAILED:
        print("\033[32m/--------------------------------\\")
        print("  Cause: \033[40m\033[94m" + response.erro_cause + "  \033[0m")
        print("\033[41m\033[93m  " + response.error.reason + "  \033[0m")
        print("\033[32m\\--------------------------------/    \033[0m")
        print("---------------------------------------")
        return None
    else:
        return response.body


def send_requests_sales_area():
    user = get_user("willy")
    req = create_dataset_request()
    req["name"] = "Crime Rate"
    req["storage_location"] = "S3"
    resp = post_user_request(user, req)
    if resp is not None:
        print(resp)

    req = create_dataset_request()
    req["name"] = "Health Problems"
    req["storage_location"] = "EBS"
    resp = post_user_request(user, req)
    if resp is not None:
        config = Config()
        if config.is_enable(Feature.DATASET_PERMISSIONS_BY_AREA):
            print("\033[41m\033[93m ERROR!!! This Dataset should not be created!  \033[0m")
        else:
            print(resp)


def send_requests_management_area():
    user = get_user("izzy")

    req = create_dataset_request()
    req["name"] = "Storms Frequency"
    req["storage_location"] = "S3"
    resp = post_user_request(user, req)
    if resp is not None:
        print(resp)

    req = create_dataset_request()
    req["name"] = "Climate Temperature Variation"
    req["storage_location"] = "EBS"
    resp = post_user_request(user, req)
    if resp is not None:
        print(resp)


def start_user_requests():
    send_requests_sales_area()
    send_requests_management_area()
