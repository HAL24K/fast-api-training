from typing import List

from fastapi import APIRouter

from apps.api.context import Context
from apps.api.domain import commands, models
from apps.api.domain.library import ObjectIdField


context = Context()
router = APIRouter()

TAG = "people"


@router.get(
    "/people/{id}",
    response_model=models.PersonModel,
    summary="Fetch a person",
    tags=[TAG],
)
async def get_person(id: ObjectIdField):
    command = commands.GetPerson(id=id)
    return context.messagebus.handle(command)


@router.post(
    "/people",
    response_model=models.PersonModel,
    summary="Add a person",
    tags=[TAG],
)
async def add_person(person: commands.AddPerson):
    return context.messagebus.handle(person)