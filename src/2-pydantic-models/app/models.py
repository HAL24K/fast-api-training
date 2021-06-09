import uuid

from pydantic import BaseModel


class ResponseModel(BaseModel):
    message: str


class PersonModel(BaseModel):
    id: uuid.UUID