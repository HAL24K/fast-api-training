import abc
from typing import Dict

from bson.objectid import ObjectId

from apps.api.domain import models, exceptions


class AbstractPeopleRepository(abc.ABC):
    def get(self, id) -> models.PersonModel:
        return self._get(id)

    @abc.abstractmethod
    def _get(self, id):
        raise NotImplementedError

    def add(self, person: models.PersonModel):
        return self._add(person)

    @abc.abstractmethod
    def _add(self, person):
        raise NotImplementedError


class MongoPersonRepository(AbstractPeopleRepository):
    def __init__(self, mongo_config):
        self.client = mongo_config.client
        self.db = self.client[mongo_config.db]
        self.collection = "people"

    def _get(self, id) -> models.PersonModel:
        doc = self.db[self.collection].find_one(dict(_id=id))

        if not doc:
            raise exceptions.EntityNotFound(f"Person with id {id!r} not found")

        return models.PersonModel(**doc)

    def _add(self, person):
        self.db[self.collection].insert(person.dict())
        return person


class InMemoryPeopleRepository(AbstractPeopleRepository):
    people: Dict[ObjectId, models.PersonModel] = {
        ObjectId("60c2866a704fb00b25276344"): models.PersonModel(
            _id=ObjectId("60c2866a704fb00b25276344"), name="Jack", age=29
        )
    }

    def _get(self, id) -> models.PersonModel:
        try:
            return self.people[id]
        except KeyError:
            raise exceptions.EntityNotFound(f"Person with id {id!r} not found")

    def _add(self, person):
        self.people[person.id] = person
        return person