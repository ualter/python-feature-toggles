import logging
from user_requests import start_user_requests


def main():
    start_user_requests()


def init_logging():
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s | %(name)-12s | %(levelname)-8s | %(message)s",
        datefmt="%m-%d %H:%M",
        filename="./feature-toggles.log",
        filemode="w",
    )
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s | %(name)s | %(levelname)s | %(message)s")
    console.setFormatter(formatter)
    # logging.getLogger('').addHandler(console)


if __name__ == "__main__":
    init_logging()
    main()
