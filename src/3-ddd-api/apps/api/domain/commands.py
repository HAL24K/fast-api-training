from pydantic import BaseModel, Field

from apps.api.domain.library import ObjectIdField
from apps.api.domain import models


class Command(BaseModel):
    pass


class AddPerson(Command):
    person: models.PersonModel


class GetPerson(Command):
    id: ObjectIdField