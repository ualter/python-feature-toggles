from model import User
from .mock_data import MockData


def get_user(user_name: str) -> User:
    return User(**MockData[user_name])
