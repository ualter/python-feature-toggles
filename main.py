from db import get_user
from server import Context, create_dataset_request, post_request


def send_requests_sales_area():
    user = get_user("willy")
    ctx = Context(user=user)

    req = create_dataset_request()
    req["name"] = "Crime Rate"
    req["storage_location"] = "S3"
    response = post_request(ctx, req)
    print(response.body)

    req = create_dataset_request()
    req["name"] = "Health Problems"
    req["storage_location"] = "EBS"
    response = post_request(ctx, req)
    print(response.body)


def send_requests_management_area():
    user = get_user("izzy")
    ctx = Context(user=user)

    req = create_dataset_request()
    req["name"] = "Storms Frequency"
    req["storage_location"] = "S3"
    response = post_request(ctx, req)
    print(response.body)

    req = create_dataset_request()
    req["name"] = "Climate Temperature Variation"
    req["storage_location"] = "EBS"
    response = post_request(ctx, req)
    print(response.body)


def send_user_requests():
    send_requests_sales_area()
    send_requests_management_area()


def main():
    send_user_requests()


if __name__ == "__main__":
    main()
