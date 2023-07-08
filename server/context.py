from config import Config


class Context:
    def __init__(self, **entries):
        self.config = Config()
        self.__dict__.update(entries)
