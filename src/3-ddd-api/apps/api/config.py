from logging.config import dictConfig

from pymongo.mongo_client import MongoClient


class MongoDbConfigClient:
    def __init__(self, uri, username, password, db):
        self.uses_password = False
        if username and password:
            self.uses_password = True
            self.connection_string = f"mongodb://{username}:{password}@{uri}/{db}"
        else:
            self.connection_string = f"mongodb://{uri}/{db}"

        self.uri = uri
        self.db = db

        self.client = MongoClient(self.connection_string)

    def __repr__(self):
        return f"<{self.__class__.__name__} (URI: {self.uri!r}, Database: {self.db!r}, Username/Password Used?: {self.uses_password!r})>"

    def __str__(self):
        return self.__repr__()


def get_mongodb_client(uri: str, db: str, username: str, password: str):
    return MongoDbConfigClient(uri=uri, username=username, password=password, db=db)


def configure_logging(log_level: str = "INFO"):
    log_config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "default": {
                "()": "uvicorn.logging.DefaultFormatter",
                "fmt": "%(levelprefix)s %(asctime)s %(message)s",
                "datefmt": "%Y-%m-%d %H:%M:%S",
            },
        },
        "handlers": {
            "default": {
                "formatter": "default",
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stderr",
            },
        },
        "loggers": {
            "app-logger": {"handlers": ["default"], "level": log_level},
        },
    }
    dictConfig(log_config)
