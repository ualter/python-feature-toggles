from db import get_user
from model import User
from server import Context, Request, ResponseStatus, create_dataset_request, post_request


def post_user_request(user: User, req: Request):
    ctx = Context(user=user)
    response = post_request(ctx, req)
    if response.status == ResponseStatus.FAILED:
        print("\033[32m/--------------------------------\\")
        print("  Cause: \033[40m\033[94m" + response.erro_cause + "  \033[0m")
        print("\033[41m\033[93m  " + response.error.reason + "  \033[0m")
        print("\033[32m\\--------------------------------/    \033[0m")
        print("---------------------------------------")
    else:
        print(response.body)


def send_requests_sales_area():
    user = get_user("willy")
    req = create_dataset_request()
    req["name"] = "Crime Rate"
    req["storage_location"] = "S3"
    post_user_request(user, req)

    req = create_dataset_request()
    req["name"] = "Health Problems"
    req["storage_location"] = "EBS"
    post_user_request(user, req)


def send_requests_management_area():
    user = get_user("izzy")

    req = create_dataset_request()
    req["name"] = "Storms Frequency"
    req["storage_location"] = "S3"
    post_user_request(user, req)

    req = create_dataset_request()
    req["name"] = "Climate Temperature Variation"
    req["storage_location"] = "EBS"
    post_user_request(user, req)


def send_user_requests():
    send_requests_sales_area()
    send_requests_management_area()


def main():
    send_user_requests()


if __name__ == "__main__":
    main()
