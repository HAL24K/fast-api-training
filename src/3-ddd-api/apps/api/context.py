import inspect
import logging
import os

from dotenv import load_dotenv

from apps.api.service_layer import handlers, messagebus
from apps.api.domain.exceptions import ConfigurationError

load_dotenv()


class ContextException(Exception):
    pass


class Context:
    instance = None

    def __init__(self):
        if not Context.instance:
            self.load()
            Context.instance = self

    def __getattr__(self, item):
        if item not in dir(self.instance):
            raise ContextException(f"Context doesn't provide {item!r}.")
        return getattr(self.instance, item)

    def all(self):
        yield self.annotation_task_repository

    def load(self):
        self.logger = logging.getLogger(__name__)

        self.load_people_repository()

        dependencies = {"people_repository": self.people_repository}

        injected_command_handlers = {
            command_type: self._inject_dependencies(handler, dependencies)
            for command_type, handler in handlers.COMMAND_HANDLERS.items()
        }

        self.messagebus = messagebus.MessageBus(
            people_repository=self.people_repository,
            command_handlers=injected_command_handlers,
        )

    def load_people_repository(self):
        self.people_repository = self._load_people_repository(
            os.getenv("REPOSITORY_BACKEND")
        )

    def _load_people_repository(self, backend):
        self.logger.info(f"Loading {backend!r} People Repository")
        if backend == "mongodb":
            from apps.api.adapters.people_repository import MongoDbPeopleRepository
            from apps.api.config import get_mongodb_client

            uri = os.getenv("MONGO_URI")
            username = os.getenv("MONGO_USERNAME")
            password = os.getenv("MONGO_PASSWORD")
            db = os.getenv("MONGO_DATABASE")
            client = get_mongodb_client(
                uri=uri, db=db, username=username, password=password
            )

            self.logger.info(client)

            return MongoDbPeopleRepository(client=client)
        else:
            from apps.api.adapters.people_repository import InMemoryPeopleRepository

            return InMemoryPeopleRepository()

    def _inject_dependencies(self, handler, dependencies):
        params = inspect.signature(handler).parameters
        deps = {
            name: dependency
            for name, dependency in dependencies.items()
            if name in params
        }
        return lambda message: handler(message, **deps)