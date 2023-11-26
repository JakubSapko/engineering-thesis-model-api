import os

import dotenv

from ..helpers.singleton import Singleton


class DBManager(metaclass=Singleton):
    def __init__(self):
        dotenv.load_dotenv()
        self.dbname = os.getenv("dbname")
        self.user = os.getenv("user")
        self.password = os.getenv("password")


if __name__ == "__main__":
    x = DBManager()
    print(x.dbname, x.user, x.password)
