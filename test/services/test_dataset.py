from db import get_user
from user_requests import post_user_request
from server import create_dataset_request


def test_create_dataset(mocker):
    # Sales area is ALLOWED to use S3 Storage Location (Feature ON)
    mocker.patch("config.Config.is_enable", return_value=True)
    user = get_user("willy")
    req = create_dataset_request()
    req["name"] = "Crime Rate"
    req["storage_location"] = "S3"
    resp = post_user_request(user, req)
    assert resp is not None

    # Sales area is NOT allowed to use EBS Storage Location (Feature ON)
    mocker.patch("config.Config.is_enable", return_value=True)
    req = create_dataset_request()
    req["name"] = "Health Problems"
    req["storage_location"] = "EBS"
    resp = post_user_request(user, req)
    assert resp is None

    # Sales area is ALLOWED to use EBS Storage Location (Feature OFF)
    mocker.patch("config.Config.is_enable", return_value=False)
    req = create_dataset_request()
    req["name"] = "Health Problems"
    req["storage_location"] = "EBS"
    resp = post_user_request(user, req)
    assert resp is not None
